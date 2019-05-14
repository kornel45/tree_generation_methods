from collections import Counter

import numpy as np

from common import plot_tree


def gen_prufer_sequence(n):
    return list(np.random.randint(0, n, (1, n - 2))[0])


def prufer_to_tree(prufer):
    T = range(0, len(prufer) + 2)
    tree = []
    deg = [1] * len(T)
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


if __name__ == '__main__':
    prufer = [4, 3, 4, 4, 4, 0, 7, 2, 4, 9]
    edges = prufer_to_tree(prufer)
    print(edges)
    plot_tree(edges)

# n_sim = 10 ** 5
# result = 0
# k = 5
# for i in range(n_sim):
#     result = prufer_to_tree(gen_prufer_sequence(k))
# print(result / n_sim)

# n_sim = 10 ** 7
# result = 0
# k = 5
# c = Counter()
# for i in range(n_sim):
#     result = sorted([tuple(sorted(x)) for x in prufer_to_tree(gen_prufer_sequence(k))], key=lambda x: x[0])
#     for x in result:
#         c[x] += 1
# print(sorted(c))
# print(c)