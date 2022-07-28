clear
close all


h = 0;

beta = logspace(-2,2,50).';
z = linspace(-50,50,1000);
T = 1./beta;

for i = numel(beta):-1:1
    f = @(q) q_func(q, z, beta(i), h).^2;
    q(i,1) = fminsearch(f,1);
end

integrand = 1 / sqrt(2*pi) * exp(-z.^2 / 2) .* log(2*cosh(beta.*sqrt(q).*z + beta*h));
free_energy = (-beta/4).*(1-q).^2 - trapz(z, integrand, 2);


figure
subplot(2,1,1)
plot(T,q,'.--', markersize=15)
set(gca,"XScale",'log')
xlabel("T")
grid on
ylim([-0.1,1.1])
title("q")
subplot(2,1,2)
plot(T,free_energy,'.--', markersize=15)
set(gca,"XScale",'log')
% set(gca,"YScale",'log')
xlabel("T")
grid on
% ylim([-0.1,1.1]) 
title("f")

function out = q_func(q, z, beta, h)
    
    integrand = 1 / sqrt(2*pi) * exp(-z.^2 / 2) .* tanh(beta*sqrt(q).*z + beta*h).^2;
    out = q - trapz(z, integrand, 2);
end