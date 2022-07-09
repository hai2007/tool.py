#!/usr/bin/python3

import math
from .. import type

# 在(a,b,c)方向位移d


def _move(d, a, b, c=0):
    sqrt = math.sqrt(a * a + b * b + c * c)
    return [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, a * d / sqrt, b * d / sqrt, c * d / sqrt, 1]

# 围绕0Z轴旋转
# 其它的旋转可以借助transform实现
# 旋转角度单位采用弧度制


def _rotate(deg):
    sin = math.sin(deg)
    cos = math.cos(deg)
    return [cos, sin, 0, 0, -sin, cos, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

# 围绕圆心x、y和z分别缩放xTimes, yTimes和zTimes倍


def _scale(xTimes, yTimes, zTimes, cx=0, cy=0, cz=0):
    return [xTimes, 0, 0, 0, 0, yTimes, 0, 0, 0, 0, zTimes, 0, cx - cx * xTimes, cy - cy * yTimes, cz - cz * zTimes, 1]

# 针对任意射线(a1,b1,c1)->(a2,b2,c2)
# 计算出二个变换矩阵
# 分别为：任意射线变成OZ轴变换矩阵 + OZ轴变回原来的射线的变换矩阵


def _transform(a1, b1, c1, a2, b2, c2):
    if(type.isNumber(a1) and type.isNumber(b1)):

        # 如果设置二个点
        # 表示二维上围绕某个点旋转
        if(not type.isNumber(c1)):
            c1 = 0
            a2 = a1
            b2 = b1
            c2 = 1

        # 只设置三个点(设置不足六个点都认为只设置了三个点)
        # 表示围绕从原点出发的射线旋转

        elif(type.isNumber(a2) or type.isNumber(b2) or type.isNumber(c2)):
            a2 = a1
            b2 = b1
            c2 = c1
            a1 = 0
            b1 = 0
            c1 = 0

        if(a1 == a2 and b1 == b2 and c1 == c2):
            raise Exception("It's not a legitimate ray!")

        sqrt1 = math.sqrt((a2 - a1) * (a2 - a1) + (b2 - b1) * (b2 - b1))
        cos1 = (b2 - b1) / sqrt1 if sqrt1 != 0 else 1
        sin1 = (a2 - a1) / sqrt1 if sqrt1 != 0 else 0

        b = (a2 - a1) * sin1 + (b2 - b1) * cos1
        c = c2 - c1

        sqrt2 = math.sqrt(b * b + c * c)
        cos2 = c / sqrt2 if sqrt2 != 0 else 1
        sin2 = b / sqrt2 if sqrt2 != 0 else 0

        return [

            # 任意射线变成OZ轴变换矩阵
            [
                cos1, cos2 * sin1, sin1 * sin2, 0,
                -sin1, cos1 * cos2, cos1 * sin2, 0,
                0, -sin2, cos2, 0,
                b1 * sin1 - a1 * cos1, c1 * sin2 - a1 * sin1 * cos2 - b1 * cos1 * \
                cos2, -a1 * sin1 * sin2 - b1 * cos1 * sin2 - c1 * cos2, 1
            ],

            # OZ轴变回原来的射线的变换矩阵
            [
                cos1, -sin1, 0, 0,
                cos2 * sin1, cos2 * cos1, -sin2, 0,
                sin1 * sin2, cos1 * sin2, cos2, 0,
                a1, b1, c1, 1
            ]

        ]

    else:
        raise Exception("a1 and b1 is required!")

# 两个4x4矩阵相乘
# 或矩阵和齐次坐标相乘


def _multiply(matrix4, param):
    newParam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0] if (len(param)*0.25 == 4) else [0, 0, 0, 0]
    for i in range(4):
        for j in range(int(len(param)*0.25)):
            newParam[j * 4 + i] = matrix4[i] * param[j * 4] + matrix4[i + 4] * param[j *
                                                                                     4 + 1] + matrix4[i + 8] * param[j * 4 + 2] + matrix4[i + 12] * param[j * 4 + 3]
    return newParam


# 列主序存储的4x4矩阵


class Render:

    # 记录着矩阵的列表
    matrix4 = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

    def __init__(self, initMatrix=[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]):
        self.matrix4 = initMatrix

    # 移动
    def move(self, dis, a, b, c=0):
        self.matrix4 = _multiply(_move(dis, a, b, c), self.matrix4)
        return self

    # 旋转
    def rotate(self, deg, a1, b1, c1=False, a2=False, b2=False, c2=False):
        matrix4s = _transform(a1, b1, c1, a2, b2, c2)
        self.matrix4 = _multiply(
            _multiply(_multiply(matrix4s[1], _rotate(deg)), matrix4s[0]), self.matrix4)
        return self

    # 缩放
    def scale(self, xTimes, yTimes, zTimes, cx=0, cy=0, cz=0):
        self.matrix4 = _multiply(
            _scale(xTimes, yTimes, zTimes, cx, cy, cz), self.matrix4)
        return self

    # 乘法
    # 可以传入一个矩阵(matrix4,flag)
    def multiply(self, newMatrix4, flag=False):
        self.matrix4 = _multiply(self.matrix4, newMatrix4) if flag else _multiply(
            newMatrix4, self.matrix4)
        return self

    # 对一个坐标应用变换
    # 齐次坐标(x,y,z,w)
    def use(self, x, y, z=0, w=1):
        # w为0表示点位于无穷远处，忽略
        return _multiply(self.matrix4, [x, y, z, w])

    # 矩阵的值
    def value(self):
        return self.matrix4
