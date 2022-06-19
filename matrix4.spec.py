#!/usr/bin/python3

import math
from basic_toolkit.math import matrix4

# [0,-4,1,1]
print(matrix4.Render().scale(1, 2, 7, 3, 4, 1).use(0, 0, 1))

# [3, 1, 0, 1]
print(matrix4.Render().rotate(math.pi / 2, 2, 1).use(2, 0))

# [4, 6, 0, 1]
print(matrix4.Render().move(5, 3, 4).use(1, 2))
