import argparse
from TwoSpin import TwoSpinSpherical
import numpy as np
import json


def main(seed, N, B, T, iterations):
    np.random.seed(seed)
    model = TwoSpinSpherical(N, B, T)
    H_array, m_array = model.flip_many_times(iterations)
    with open(f'{N}_{B}_{T}.json', 'w') as f:
        data = dict(m_init=m_array[0], m_final=m_array[-1],
                    H_init=H_array[0], H_final=H_array[-1])
        json.dump(data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Two spin spherical model')
    parser.add_argument('seed', type=int)
    parser.add_argument('N', type=int)
    parser.add_argument('B', type=float)
    parser.add_argument('T', type=float)
    parser.add_argument('iterations', type=int)

    args = parser.parse_args()
    main(**args.__dict__)
