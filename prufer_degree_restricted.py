"""
Moduł zawiera funkcje do:
 - generowania ciągów Prufera o ograniczonym stopniu wierzchoka
 - symulację symulującą rozkład drzew wygenerowanych za pomocą kodowania Prufera
"""
from collections import Counter

import matplotlib.pyplot as plt
import numba
import numpy as np


@numba.jit(nopython=True)
def gen_tree(n, d):
    result = np.random.randint(0, n, (1, n - 2))[0]
    while not is_correct(result, d):
        result = np.random.randint(0, n, (1, n - 2))[0]
    return result


@numba.jit(nopython=True)
def most_frequent(iter):
    return np.bincount(iter).max()


@numba.jit(nopython=True)
def is_correct(pruf, d):
    return most_frequent(pruf) < d


if __name__ == '__main__':
    d = 3
    x = range(5, 6)
    for i in x:
        c = Counter()
        for _ in range(10 ** 5):
            pruf = gen_tree(i, d)
            c[tuple(pruf)] += 1
        labels, values = zip(*c.items())
        indexes = [str(x) for x in labels]
        width = 1
        weights = np.ones_like(values) / float(sum(values))
        plt.bar(range(len(weights)), np.array(values) * weights, width)
        plt.xticks(rotation=90)
        plt.show()
