import random
from collections import Counter

from common import plot_tree


def fast_random_tree(n):
    """
    https://link.springer.com/content/pdf/10.1007/3-540-44862-4_95.pdf
    """
    I = list(range(n))  # Initial vector of node numbers
    edges = [None for _ in range(n - 1)]
    root = random.randint(0, n-1)
    I[root], I[0] = I[0], I[root]
    for m in range(0, n - 1):
        t = random.randint(0, m)  # new node
        s = random.randint(m + 1, n - 1)
        edges[m] = (I[t], I[s])  # adding edgde
        I[m + 1], I[s] = I[s], I[m + 1]  # replaceing from n-m+1 to n - nodes that are in a tree already
    return edges


# if __name__ == '__main__':
#     edges = fast_random_tree(5)
#     print()


n_sim = 10 ** 7
result = 0
k = 10
c = Counter()
for i in range(n_sim):
    result = sorted([tuple(sorted(x)) for x in fast_random_tree(5)], key=lambda x: x[0])
    for x in result:
        c[x] += 1
print(sorted(c))
print(c)