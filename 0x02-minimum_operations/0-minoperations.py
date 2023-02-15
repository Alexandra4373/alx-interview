#!/usr/bin/python3

""" Minimum Operations"""


def minOperations(n):
    if not isinstance(n, int):
        return 0
    op = 0
    iter = 2
    while (iter <= n):
        if not(n % iter):
            n = int(n / iter)
            op += iter
            iter = 1
        iter += 1
    return op
