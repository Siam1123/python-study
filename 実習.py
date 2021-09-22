# foo = 10.55
# print(foo, type(foo))

# #四捨五入する
# foo = round(foo)
# print( foo, type(foo))

# moji ="abc" + "def"
# print(moji)

# def kansu():
#     a = 100
#     b = 200
#     return a,b

# x , y = kansu()

# print(kansu(x))
# try:
#     a = int(input("整数を入力してください"))
#     if a == 50:
#         raise ValueError
#     print(100 // a)

# except ZeroDivisionError:
#     print("ゼロによる除算が行われました")

# except:
#     print("何らかの例外が発生しました")

# else:
#     print("正常終了")

# finally:
#     print("お疲れさまでした")

# class Member:
#     pass

# yamada = Member()
# yamada.no = 15
# yamada.name = "山田太郎"
# yamada.weight = 72.7

# sekine = Member()
# sekine.no = 37
# sekine.name = "関根信彦"
# sekine.weight = 65.3

# print("{}: {} {}kg".format(yamada.no,yamada.name,yamada.weight))
# print("{}: {} {}kg".format(sekine.no,sekine.name,sekine.weight))

# f = open("hello.txt", "w")
# f.write("Hello!\n")
# f.write("How are you?\n")
# f.close()

# f = open("hello.txt")
# line1 = f.readline()
# line2 = f.readline()

# print(line1, end="")
# print(line2, end="")

# f.close()

f = open("hello.txt","a")

f.write("Fine, thank.\n")
f.write("And you?\n")

f.close()