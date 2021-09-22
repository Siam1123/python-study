#11-1
# import math

# class Circle:
#     PI = 3.1415

#     def calc_circmference(self, radius):
#         res = 2 * Circle.PI * radius 
#         return math.floor(res * 10 ** 3) /(10 ** 3)

#     def calc_area(self, radius):
#         res = Circle.PI * radius ** 2
#         return math.floor(res * 10 ** 3)/(10 ** 3)

# class Main:

#     def execute(self):
#         circle = Circle()
#         radius = int(input("半径を整数値で入力："))
#         circumference = circle.calc_circmference(radius)

#         area = circle.calc_area(radius)

#         print("円周の長さは{}です".format(circumference))
#         print("円の面積は{}です".format(area))

# main = Main()
# main.execute()

#11-2
class CalcExecutor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self) -> int:
        res = 0
        for num in range(self.x, self.y + 1):
            res += num
        return res

class Main:

    def execute(self) -> None:
        calc_exec = CalcExecutor(100, 200)
        total = calc_exec.sum
        print("{}から{}の合計値は{}です".format(calc_exec.x, calc_exec.y, total))

main = Main()
main.execute()

#11-3