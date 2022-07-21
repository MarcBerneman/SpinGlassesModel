import numpy as np


class TwoSpin:
    def __init__(self, N: int, B: float = 0.0, T: float = 0.0):
        self.B = B
        self._k = 1
        self._T = None
        self._beta = None
        self.setT(T)

        self._N = None
        self._J = None
        self._A = None
        self.s = None
        self.setN(N)

    def H(self):
        return - (self.s.T @ self._A @ self.s).item() - self.B * self.s.sum()

    def setT(self, T: float):
        self._T = T
        if self._T == 0.0:
            self._beta = float('inf')
        else:
            self._beta = 1 / (self._k * self._T)

    def setN(self, N):
        self._N = N
        self._J = 1 / N
        self._A = self._J * (np.ones(N) - np.eye(N))
        self.s = np.ones(shape=(N, 1))


class TwoSpinDiscrete(TwoSpin):
    def __init__(self, N: int, B: float = 0.0, T: float = 0.0):
        super().__init__(N, B, T)
        self.s = np.random.randint(2, size=(N, 1)) * 2 - 1

    def __flip_spin(self):
        idx = np.random.randint(self._N)
        H_before = self.H()
        self.s[idx] = - self.s[idx]
        H_after = self.H()
        DeltaH = H_after - H_before
        if self._T == 0.0:
            relative_prob = 0.0 if DeltaH > 0 else 1.0
        else:
            relative_prob = np.exp(- self._beta * DeltaH)
        accept = relative_prob >= np.random.rand()
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


class TwoSpinSpherical(TwoSpin):
    def __init__(self, N: int, B: float = 0.0, T: float = 0.0):
        super().__init__(N, B, T)
        self.s = np.random.randn(N, 1)
        self.normalize()

    def __random_walk(self):
        s_before = self.s.copy()
        H_before = self.H()
        self.s += np.random.randn(self._N, 1) / self._N
        self.normalize()
        H_after = self.H()
        DeltaH = H_after - H_before
        if self._T == 0.0:
            relative_prob = 0.0 if DeltaH > 0 else 1.0
        else:
            relative_prob = np.exp(- self._beta * DeltaH)
        accept = relative_prob >= np.random.rand()
        if not accept:
            self.s = s_before

    def flip_many_times(self, times: int):
        H_array = np.zeros(shape=(times,))
        m_array = np.zeros(shape=(times,))
        for i in range(times):
            H_array[i] = self.H()
            m_array[i] = self.s.mean()
            self.__random_walk()
        return H_array, m_array

    def normalize(self):
        self.s *= np.sqrt(self._N / np.square(self.s).sum())
