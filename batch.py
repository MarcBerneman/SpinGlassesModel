import argparse
from TwoSpin import TwoSpinSpherical
import numpy as np
import json
from pathlib import Path


def main(seed: int, N: int, B: float, T: float, iterations: int, save_folder: Path):
    save_file = save_folder / f'{N}_{B}_{T}_{iterations}' / f"{seed}.json"
    if save_file.exists():
        return
    save_file.parent.mkdir(parents=True, exist_ok=True)

    np.random.seed(seed)
    model = TwoSpinSpherical(N, B, T)
    H_array, m_array = model.flip_many_times(iterations)

    indices = np.linspace(-1, iterations-1, 11).round().astype(int)
    indices[0] = 0
    with open(save_file, 'w') as f:
        data = dict(indices=indices, m=m_array[indices], H=H_array[indices])
        for key in data.keys():
            data[key] = data[key].tolist()
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
