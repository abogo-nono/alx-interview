#!/usr/python3
"""
0. Pascal triangle
"""


def pascal_triangle(n):
    """generate a pascal triangle base on user input

    Args:
        n (int): the number of line of the triangle

    Returns:
        list: the list containing the triangle element (if n > 0)
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
