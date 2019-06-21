"""
Moduł zawiera funkcje do:
 - generowania ciągów Fast Random Tree
 - symulację symulującą rozkład drzew wygenerowanych za pomocą Fast Random Tree
 """
import random
from collections import Counter

import matplotlib.pyplot as plt
import numba
import numpy as np

from prufer import tree_to_prufer


@numba.jit(nopython=True)
def fast_random_tree(n):
    I = list(range(n))
    edges = []
    root = random.randint(0, n - 1)
    I[root], I[0] = I[0], I[root]
    for m in range(0, n - 1):
        t = random.randint(0, m)
        s = random.randint(m + 1, n - 1)
        edges.append((I[t], I[s]))
        I[m + 1], I[s] = I[s], I[m + 1]
    return edges


def simulation(k):
    c = Counter()
    result = sorted([tuple(sorted(x)) for x in fast_random_tree(k)])
    for x in result:
        c[x] += 1
    return c


def f(n):
    result = 0
    for i in range(1, n):
        result += 1 / i
    return result


if __name__ == '__main__':
    x = range(3, 6)
    d = 3
    for i in x:
        c = Counter()
        for _ in range(10 ** 5):
            tree = fast_random_tree(i)
            pruf = tree_to_prufer(tree.copy())

            c[tuple(pruf)] += 1
        labels, values = zip(*c.items())
        indexes = [str(x) for x in labels]
        width = 1
        weights = np.ones_like(values) / float(sum(values))
        plt.bar(range(len(weights)), np.array(values) * weights, width)
        plt.xticks(rotation=90)
        plt.show()
