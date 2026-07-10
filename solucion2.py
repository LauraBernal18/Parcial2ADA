#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    tree = {}

    for i in range(len(indexes)):
        tree[i + 1] = indexes[i][:]

    result = []

    for k in queries:

        stack = [(1, 1)]

        while stack:
            node, depth = stack.pop()

            if node == -1:
                continue

            if depth % k == 0:
                tree[node][0], tree[node][1] = tree[node][1], tree[node][0]

            left, right = tree[node]

            if right != -1:
                stack.append((right, depth + 1))

            if left != -1:
                stack.append((left, depth + 1))

        # In-order iterativo
        ans = []

        stack = []

        current = 1

        while stack or current != -1:

            while current != -1:
                stack.append(current)
                current = tree[current][0]

            current = stack.pop()

            ans.append(current)

            current = tree[current][1]

        result.append(ans)

    return result

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'resultado2.txt')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
