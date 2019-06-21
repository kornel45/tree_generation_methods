"""
Moduł zawiera funkcje do:
 - generowania ciągów Prufera
 - generowania drzewa z ciągu Prufera
 - generowanie ciągu z kodu Prufera
 - symulację symulującą rozkład drzew wygenerowanych za pomocą kodowania Prufera
"""
from collections import defaultdict, Counter

import matplotlib.pyplot as plt
import numba
import numpy as np


def gen_prufer_sequence(n):
    return list(np.random.randint(0, n, (1, n - 2))[0])


def prufer_to_tree(prufer):
    T = numba.prange(0, len(prufer) + 2)
    tree = []
    deg = [1 for _ in range(len(prufer) + 2)]
    for i in prufer:
        deg[i] += 1
    for i in prufer:
        for j in T:
            if deg[j] == 1:
                tree.append((i, j))
                deg[i] -= 1
                deg[j] -= 1
                break

    last = [x for x in T if deg[x] == 1]
    tree.append((last[0], last[1]))
    return tree


def tree_to_prufer(tree):
    n = len(tree) + 2
    d = defaultdict(int)
    L = []
    for edge in tree:
        d[edge[0]] += 1
        d[edge[1]] += 1
    for i in range(n - 2):
        for x in range(n):
            if d[x] == 1:
                break
        y = None
        for edge in tree:
            if x == edge[0]:
                y = edge[1]
            elif x == edge[1]:
                y = edge[0]
            if y is not None:
                break
        L.append(y)
        for j in (x, y):
            d[j] -= 1
            if not d[j]:
                d.pop(j)
        tree.remove(edge)
    return L[:-1]


def simulation(k):
    k = 100
    c = Counter()
    result = sorted([tuple(sorted(x)) for x in prufer_to_tree(gen_prufer_sequence(k))])
    for x in result:
        c[x] += 1
    return c


def most_frequent(iter):
    return np.bincount(iter).max()


if __name__ == '__main__':
    x = range(5, 6)
    d = 3
    for i in x:
        c = Counter()
        for _ in range(10 ** 6):
            pruf = gen_prufer_sequence(i)

            c[tuple(pruf)] += 1
        labels, values = zip(*c.items())
        indexes = [str(x) for x in labels]
        width = 1
        weights = np.ones_like(values) / float(sum(values))
        plt.bar(range(len(weights)), np.array(values) * weights, width)
        plt.xticks(rotation=90)
        plt.show()
