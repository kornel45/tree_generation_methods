import random
from collections import Counter

import matplotlib.pyplot as plt
import numba
import numpy as np

from prufer import tree_to_prufer


@numba.jit(nopython=True)
def gen_tree(n, d):
    I = list(range(n))
    edges = []
    root = random.randint(0, n - 1)
    degrees = [0] * n
    I[root], I[0] = I[0], I[root]
    m = 0
    k = 1
    while m < n - k:
        t = random.randint(0, m)
        s = random.randint(m + 1, n - k)
        edges.append((I[t], I[s]))
        degrees[I[t]] += 1
        degrees[I[s]] += 1
        I[m + 1], I[s] = I[s], I[m + 1]
        if degrees[I[t]] == d:
            I[t], I[n - k] = I[n - k], I[t]
            I[t], I[m + 1] = I[m + 1], I[t]
            k += 1
        else:
            m += 1
    return edges


if __name__ == '__main__':
    x = range(3, 4)
    d = 4
    for i in x:
        c = Counter()
        for _ in range(10 ** 5):
            pruf = tree_to_prufer(gen_tree(i, d))

            c[tuple(pruf)] += 1
        labels, values = zip(*c.items())
        indexes = [str(x) for x in labels]
        width = 1
        weights = np.ones_like(values) / float(sum(values))
        plt.bar(range(len(weights)), np.array(values) * weights, width)
        plt.xticks(rotation=90)
        plt.show()
