#共通問題１－１
# print("あいうえお")

#共通問題１－２
# print("a,bc")
# print("d,e")

#共通問題１－３
# print("１｜２｜３，４，５")

#共通問題１－４
# print("あいうえお")
# print("かきくけこ")

#共通問題１－５
# print(12,"あいうえお")

#共通問題１－６
# capital = "東京"
# prefectures = 47

# print("日本の首都は",capital)
# print("都道府県は",prefectures)

#共通問題１－７
# capital = "東京"
# area = 2193

# print("日本の首都は",capital, sep="---",end="---")
# print("面積（㎢）は",area, sep="---")

#共通問題１－８
# print("吾輩は猫である。",end="")
# print("名前はまだない。",end="")
# print("どこで生まれたか頓と見当がつかぬ。",end="")
# print("何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。",
# end="")
# print("吾輩はここで初めて人間というものを見た。")

#共通問題１－９
# mag = input("お名前を入力してください＞")
# print("こんにちは", mag, "さん！", sep="")

#共通問題１－１０
# mozi = input("文字の入力：")
# seisu = input("整数値の入力：")
# syousu = input("少数の入力：")
# print("入力された文字＝",mozi)
# print("入力された整数＝",seisu)
# print("入力された少数＝",syousu)

#共通問題１－１１
# from typing import DefaultDict

# year = input("年：")
# month = input("月：")
# day = input("日：")

# print(year,"/",month,"/",day)

#共通問題２－１
# a = 1
# b = "True"
# c = ""
# d = 10.0

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

#共通問題２－２
# a = 10
# b = "10"
# c = "十"

# a = int(a)
# print(type(a)) 

# b = int(b)
# print(type(b))

# c = int(c) #変換できません
# print(type(c))

#共通問題２－３
# a = 100
# b = 100.0
# c = -100

# a = str(a)
# print(type(a))

# b = str(b)
# print(type(b))

# c = str(c)
# print(type(c)) 

#共通問題２－４
# a = "ob1010" #１進数
# b = "12" #８進数
# c = "A" #１６進数

# print(a)
#進数の変換のやり方がわからない

#共通問題３－１
# a = 12 + 34
# print("12 + 34 =", a)

#共通問題３－２
# a = 98 - 76
# print("98 - 76 =", a)

#共通問題３－３
# a = 23 * 45
# print("23 × 45 =", a)

#共通問題３－４
# a = 56 / 14
# print("56 ÷ 14 =",a)

#共通問題３－５
# a = 66//9
# print("66 // 9 =",a)

#共通問題３－６
# a = 7%3
# print("7 % 3 =",a)

#共通問題３－７
# menseki = 6 * 5 / 2
# print(menseki)

#共通問題３－８
# menseki = (5 + 8) * 6 / 2
# print(menseki)

#共通問題３－９
# r = 3
# p = 3.14
# menseki = r * r * p
# print(menseki)

#共通問題３－１０
# mozi_a = "abc"
# mozi_b = "xyz"

# print(mozi_a + mozi_b)

#共通問題３－１１
# mozi_a = input("文字列１：")
# mozi_b = input("文字列２：")
# print(mozi_b + mozi_a)

#共通問題３－１２
# a = 1 + 2   #3
# b = 7 + 7 / 7 + 7   #15
# c = 7 + 7 * 7 / 7 + 7   #21
# d = 7 + (7 + 7 * 7 / 7 + 7) #28
# e = 1 + 2 // 3 - 4 % 5 ** 2 #-3
# f = 100 == "100"    #エラー

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

#共通問題３－１３
# num1 = 100
# num2 = 200
# sum = (num1 + num2)
# print(sum)

#共通問題３－１４
# print("四角形の面積を求めます")
# vertical= float(input("縦の長さ："))
# horizontal = float(input("横の長さ："))
# area = vertical * horizontal
#print("四角形の面積＝",area )

#共通問題３－１５
# print("三角形の面積を求めます")
# bottom = float(input("底辺の長さ："))
# height = float(input("高さ；"))
# print("三角形の面積：",bottom * height / 2)

#共通問題３－１６
# print("円の面積を求めます")
# r = float(input("半径："))
# PI = 3.14159
# print("円の面積=",r ** 2 * PI)

#共通問題３－１７
# print("台形の面積を求めます")
# upper = float(input("上底の長さ："))
# bottom = float(input("下底の長さ："))
# height = float(input("高さ；"))
# print("台形の面積=",(upper + bottom) * height / 2)

#共通問題３－１８
# print("税込価格を求めます")

# price = int(input("定価："))
# tax = int(input("消費税率："))
# result = price + (price * (tax / 100))

# print("定価:",price)
# print("税率：",tax)
# print("税込価格：",result)

#共通問題３－１９
print("BMI値を求めます")

cm = float(input("身長（ｃｍ）："))
weight = float(input("体重（ｋｇ）："))

height = cm / 100

BMI = weight / (height * height)

print("BMI値=",BMI)