clear
close all

syms q
n = 5;

Q_vec = sym('Q',[1,nchoosek(n,2)]);
Q = sym(zeros(n));
idx = [1,n-1];
for i = 1:n-1
    Q(i,i+1:end) = Q_vec(idx(1):idx(2));
    idx(1) = idx(2) + 1;
    idx(2) = idx(2) + n - i - 1 ;
end
Q = Q + Q.'; % make it symmetric

g = trace(Q^2);
grad = gradient(g, Q_vec); % ==> Q1 = ... = Qn = 0 => Q = 0
hess = hessian(g, Q_vec); % diagonal matrix (4*eye(n))
eig(hess) % all positive (4) => Q = 0 is a minimum