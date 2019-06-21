"""
Moduł zawiera funkcje do:
 - symulacji czasowej Prufera
 - symulacji czasowej Fast Random Tree
 - symulację symulującą rozkład drzew wygenerowanych za pomocą Fast Random Tree
"""

import time
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from prufer import gen_prufer_sequence, prufer_to_tree, tree_to_prufer
from fast_random_tree import fast_random_tree


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result

    return timed


def check_fast_random_tree(n, k):
    print('Zaczynam liczyć fast random tree')
    s = time.time()
    for i in range(n):
        fast_random_tree(k)
    e = time.time()
    print(e - s)


def check_prufer_generation(n, k):
    print('Zaczynam liczyć prufer sequence')
    s = time.time()
    for i in range(n):
        prufer_to_tree(gen_prufer_sequence(k))
    e = time.time()
    print(e - s)


@timeit
def plot_fast_random_tree(n, k):
    x = range(3, n, n // k)
    result = []
    for i in x:
        s = time.time()
        fast_random_tree(i)
        e = time.time()
        result.append(e - s)
    return x, result


@timeit
def plot_prufer_sequence(n, k):
    x = range(3, n, n // k)
    result = []
    for i in x:
        s = time.time()
        prufer_to_tree(gen_prufer_sequence(i))
        e = time.time()
        result.append(e - s)
    return x[1:], result[1:]


def plot_hist_frd(n, k):
    resulted_trees = Counter()
    for i in range(n):
        resulted_trees[tuple(tree_to_prufer(fast_random_tree(k)))] += 1
    return resulted_trees


if __name__ == '__main__':
    c = plot_hist_frd(10 ** 5, 5)
    labels, values = zip(*c.items())
    tmp_help = sorted(zip(values, labels))
    values, labels = zip(*tmp_help)
    indexes = [str(x) for x in labels]
    width = 1
    weights = np.ones_like(values) / float(sum(values))
    plt.bar(range(len(weights)), np.array(values) * weights, width)#, edgecolor='black', color='white')
    plt.xticks(rotation=90)
    plt.title('Ilość występowania poszczególnych drzew w Fast Random Tree')
    plt.xlabel('Drzewo zakodowane do sekwencji Prufera')
    plt.ylabel('Częstotliwość wystąpienia')
    plt.show()

