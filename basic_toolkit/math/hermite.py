#!/usr/bin/python3

# Hermite三次插值

class Render:

    # 张弛系数
    u = 0.5

    # 边界坐标
    a = 0
    b = 1

    # 暂存
    MR = [0, 0, 0, 0]
    isSetP = False

    def __init__(self, u=0.5):
        self.u = u

    def setP(self, x1, y1, x2, y2,  s1, s2):
        if(x1 < x2):

            # 记录原始尺寸
            self.a = x1
            self.b = x2

            p3 = self.u * s1
            p4 = self.u * s2

            # 缩放到[0,1]定义域
            y1 /= (x2 - x1)
            y2 /= (x2 - x1)

            # MR是提前计算好的多项式通解矩阵
            # 为了加速计算
            # 如上面说的
            # 统一在[0,1]上计算后再通过缩放和移动恢复
            # 避免了动态求解矩阵的麻烦

            self.MR[0] = 2 * y1 - 2 * y2 + p3 + p4
            self.MR[1] = 3 * y2 - 3 * y1 - 2 * p3 - p4
            self.MR[2] = p3
            self.MR[3] = y1

            self.isSetP = True

            return self

        else:
            raise Exception("The point x-position should be increamented!")

    def valueOf(self, x):
        if(self.isSetP):
            sx = (x - self.a) / (self.b - self.a)
            sx2 = sx * sx
            sx3 = sx * sx2
            sResult = sx3 * self.MR[0] + sx2 * \
                self.MR[1] + sx * self.MR[2] + self.MR[3]
            return sResult * (self.b - self.a)
        else:
            raise Exception("You shoud first set the position!")
