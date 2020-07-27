from random import random
from time import time
import sys


def throw_dart():
    x = random()
    y = random()

    if (x * x) + (y * y) <= 1:
        return 1

    return 0


def main(iterations: int):
    hits = 0
    start = time()

    for i in range(0, iterations):
        hits = hits + throw_dart()

    end = time()
    pi = (4 * hits) / iterations
    print(pi)
    print(f"Execution time: {end - start} seconds.")


if __name__ == "__main__":
    main(int(sys.argv[1]))
