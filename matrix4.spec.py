#!/usr/bin/python3

from basic_toolkit.math import matrix4

# [0,-4,1,1]
print(matrix4.Render([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
      0, 0, 0, 1]).scale(1, 2, 7, 3, 4, 1).use(0, 0, 1))
