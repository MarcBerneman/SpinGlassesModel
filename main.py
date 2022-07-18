import numpy as np

from TwoSpin import TwoSpin
import matplotlib.pyplot as plt


def singleTsingleB(T, B):
    N = 100
    model = TwoSpin(N, T=T, B=B)
    H_array, m_array = model.flip_many_times(1000)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(m_array)
    ax[0].set_ylim(-1.1, 1.1)
    ax[1].plot(H_array)
    for ax_ in ax:
        ax_.grid()
    plt.show()


def varyB(T, B_array):
    N = 100
    model = TwoSpin(N, T=T, B=0)
    H_array = np.zeros_like(B_array)
    m_array = np.zeros_like(B_array)
    for i, B in enumerate(B_array):
        model.B = B
        __H_array, __m_array = model.flip_many_times(1000)
        H_array[i] = __H_array[-1]
        m_array[i] = __m_array[-1]

    fig, ax = plt.subplots(1, 1)
    ax.plot(B_array, m_array, 'b.--', linewidth=2, markersize=15)
    ax.set_ylim(-1.1, 1.1)
    ax.grid()
    plt.show()


def varyT(B, T_array):
    N = 100
    model = TwoSpin(N, T=0.0, B=B)
    H_array = np.zeros_like(T_array)
    m_array = np.zeros_like(T_array)
    for i, T in enumerate(T_array):
        model.setT(T)
        __H_array, __m_array = model.flip_many_times(1000)
        H_array[i] = __H_array[-1]
        m_array[i] = __m_array[-1]

    fig, ax = plt.subplots(1, 1)
    ax.plot(T_array, m_array, 'b.--', linewidth=2, markersize=15)
    ax.set_ylim(-1.1, 1.1)
    ax.grid()
    plt.show()


if __name__ == '__main__':
    # singleTsingleB(0.01, 0.1)

    # B_array = np.concatenate((np.linspace(-2, 2, 20), np.linspace(2, -2, 20)))
    # varyB(0.0, B_array)

    T_array = np.concatenate((np.linspace(0, 4, 20), np.linspace(4, 0, 20)))
    varyT(0.0, T_array)
