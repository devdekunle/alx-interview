#!/usr/bin/python3
"""
function that computes the pascal triangle of a given number
"""


def pascal_triangle(n):
    """
    returns the pascal triangle of a given number
    """
    if n <= 0:
        return []

    pascal_list = []
    pascal_list.append([1])
    for i in range(1, n):
        pascal_list.append([])
        pascal_list[i].append(1)
        for j in range(1, i):
            pascal_list[i].append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        pascal_list[i].append(1)

    return pascal_list
