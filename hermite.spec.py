#!/usr/bin/python3

from basic_toolkit.math import hermite

h = hermite.Render(1)
h.setP(0, 1, 3, 28, 0, 27)

# 1
print("x=0,y=", h.valueOf(0))
#  2
print("x=1,y=", h.valueOf(1))
#  9
print("x=2,y=", h.valueOf(2))
# 28
print("x=3,y=", h.valueOf(3))
