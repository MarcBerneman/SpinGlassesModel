import numpy as np


class TwoSpin:
    def __init__(self, N: int, B: float = 0.0, T: float = 0.0):
        self.N = N
        self.B = B
        self.__k = 1
        self.__T = None
        self.__beta = None
        self.setT(T)
        self.s = np.random.randint(2, size=(N, 1)) * 2 - 1
        self.__J = 1 / N
        self.__A = self.__J / 2 * (np.ones(N) - np.eye(N))

    def H(self):
        return - (self.s.T @ self.__A @ self.s).item() - self.B * self.s.sum()

    def __flip_spin(self):
        idx = np.random.randint(self.N)
        H_before = self.H()
        self.s[idx] = - self.s[idx]
        H_after = self.H()
        DeltaH = H_after - H_before
        if DeltaH <= 0:
            accept = True
        else:
            if self.__T == 0.0:
                relative_prob = 0.0
            else:
                relative_prob = np.exp(- self.__beta * DeltaH)
            if relative_prob > np.random.rand():
                accept = True
            else:
                accept = False
        if not accept:
            self.s[idx] = - self.s[idx]  # undo the flipping

    def flip_many_times(self, times: int):
        H_array = np.zeros(shape=(times,))
        m_array = np.zeros(shape=(times,))
        for i in range(times):
            H_array[i] = self.H()
            m_array[i] = self.s.mean()
            self.__flip_spin()
        return H_array, m_array

    def setT(self, T: float):
        self.__T = T
        if self.__T == 0.0:
            self.__beta = float('inf')
        else:
            self.__beta = 1 / (self.__k * self.__T)
