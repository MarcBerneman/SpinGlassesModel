import argparse
from TwoSpin import TwoSpinSpherical
import numpy as np
import json
from pathlib import Path


def main(seed: int, N: int, B: float, T: float, iterations: int, save_folder: Path):
    np.random.seed(seed)
    model = TwoSpinSpherical(N, B, T)
    H_array, m_array = model.flip_many_times(iterations)
    save_file = save_folder / f'{N}_{B}_{T}' / f"{seed}.json"
    save_file.parent.mkdir(parents=True, exist_ok=True)
    with open(save_file, 'w') as f:
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
    parser.add_argument('save_folder', type=Path)

    args = parser.parse_args()
    main(**args.__dict__)
