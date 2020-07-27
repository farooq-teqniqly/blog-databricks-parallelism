from random import random
from time import time
from multiprocessing import Pool
import sys


def throw_dart(iterations: int) -> int:
    hits = 0

    for i in range(iterations):
        x = random()
        y = random()

        if (x * x) + (y * y) <= 1:
            hits = hits + 1

    return hits


def main(iterations: int, process_count: int):
    pool = Pool(processes=process_count)
    trials_per_process = [int(iterations / process_count)] * process_count

    start = time()

    hits = pool.map(throw_dart, trials_per_process)
    pi = (sum(hits) * 4) / iterations

    end = time()

    print(pi)
    print(f"Execution time: {end - start} seconds.")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
