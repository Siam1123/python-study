# for _ in range(10):
#     print("Hello")

#９－２
#関数定義
# def hello():
#     for _ in range(10):
#         print("Hello")

#関数の呼び出し
# hello()

#９－１
# def school_name(school, name):
#     print("学校名：",school)
#     print("名前：",name)

# school = "東京情報クリエイター工学院専門学校"
# name = "竹井一馬"

# school_name(school,name)

#9-3
# def put_str(moji, count):

#     for _ in range(count):
#         print(moji)


# put_str("hello",3)
# put_str("good morning",4)
# put_str("good evening",2)

#9-4
# def triple(num):
#     return num * 3

# input_num = int(input("整数を入力してください："))

# triple_num = triple(input_num)
# ninetimes_num = triple(triple_num)

# print(input_num,"の9倍は",ninetimes_num,"です。" )

#9-5
# def add(num1, num2):
#     # 引数に指定された２つの値を足し算して返却する
#     result = num1 + num2

#     return result

# def sub(num1, num2):
#     # 引数に指定された２つの値を引き算して返却する
#     mul = num1 - num2
    
#     return result

# def mul(【穴埋め3】, num2):
#     # 引数に指定された２つの値を掛け算して返却する
#     result = num1 * num2
    
#     return result

# def div(num1, num2):
#     # 引数に指定された２つの値を割り算して返却する
#     if 【穴埋め4】:
#         # 割る数が0の場合は割り算を行わず0を返却する
#         result = 0
#     else:
#         result = num1 / num2

#     return result

# def rem(num1, num2):
#     # 引数に指定された２つの値を剰余算して返却する
#     if num2 == 0:
#         # 割る数が0の場合は剰余算を行わず割られる数を返却する
#         result = num1
#     else:
#         result = num1 % num2

#     return result

# # メイン処理
# input_num1 = int(input("1つ目の整数："))
# input_num2 = int(input("2つ目の整数："))

# # 足し算
# add_result = 【穴埋め5】
# print(input_num1, "+", input_num2, "=", 【穴埋め6】, sep="")

# # 引き算
# sub_result = sub(input_num1, input_num2)
# print(input_num1, "-", input_num2, "=", sub_result, sep="")

# # 掛け算
# mul_result = mul(input_num1, input_num2)
# print(input_num1, "*", input_num2, "=", mul_result, sep="")

# # 割り算
# div_result = div(input_num1, input_num2)
# print(input_num1, "/", input_num2, "=", div_result, sep="")

#9-6
