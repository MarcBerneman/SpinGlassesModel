import numpy as np
from TwoSpin import TwoSpinDiscrete, TwoSpinSpherical
import matplotlib.pyplot as plt


def singleTsingleB(model, times=1000):
    H_array, m_array = model.flip_many_times(times)
    fig, ax = plt.subplots(3, 1, sharex='all')
    ax[0].plot(m_array)
    ax[0].set_ylim(-1.1, 1.1)
    ax[1].plot(H_array)
    for ax_ in ax:
        ax_.grid()
    plt.show()


def varyB(model, B_array, times=1000):
    H_array = np.zeros_like(B_array)
    m_array = np.zeros_like(B_array)
    for i, B in enumerate(B_array):
        model.B = B
        __H_array, __m_array = model.flip_many_times(times)
        H_array[i] = __H_array[-1]
        m_array[i] = __m_array[-1]

    fig, ax = plt.subplots(1, 1)
    ax.plot(B_array, m_array, 'b.--', linewidth=2, markersize=15)
    ax.set_ylim(-1.1, 1.1)
    ax.grid()
    plt.show()


def varyT(model, T_array, times=1000):
    H_array = np.zeros_like(T_array)
    m_array = np.zeros_like(T_array)
    for i, T in enumerate(T_array):
        model.setT(T)
        __H_array, __m_array = model.flip_many_times(times)
        H_array[i] = __H_array[-1]
        m_array[i] = __m_array[-1]

    fig, ax = plt.subplots(1, 1)
    ax.plot(T_array, m_array, 'b.--', linewidth=2, markersize=15)
    ax.set_ylim(-1.1, 1.1)
    ax.grid()
    plt.show()


def main():
    np.random.seed(0)
    N = 100
    T = 0.0
    B = 0.0
    model = TwoSpinDiscrete(N=N, T=T, B=B)
    model.setRandomCoupling(1.0)

    singleTsingleB(model, 1000)

    # B_array = np.concatenate((np.linspace(-2, 2, 20), np.linspace(2, -2, 20)))
    # varyB(model_(N=N, T=T, B=B), B_array)

    # model_.B = 0.0
    # T_array = np.concatenate((np.linspace(0, 4, 20), np.linspace(4, 0, 20))) / 4
    # varyT(model_, T_array, 1000)
    # singleTsingleB(model_, 20000)


if __name__ == '__main__':
    main()
