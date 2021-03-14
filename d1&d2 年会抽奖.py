import random
import string

# Exercise 11.2
"""
写个匹配成绩的小程序，要求用户输入0-100的数字后，你能正确打印他的对应成绩等级，比如输入的是75，则打印C
"""

print("我是帅气的分割线".center(100, "-"))

mark = float(input("请输入您的成绩："))
if 90 <= mark <= 100:
    print("A")
elif 80 <= mark < 90:
    print("B")
elif 60 <= mark < 80:
    print("C")
elif 40 <= mark < 60:
    print("D")
else:
    print("E")

print("我是帅气的分割线".center(100, "-"))


# Exercise 3.3
"""
下三角矩阵格式打印99乘法口诀表,两种方法
:string.join(seq): 以string作为分隔符，串接seq。
"""
# 方法一
print("方法一:")
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}×{} = {}   ".format(i, j, i*j), end="")
        if i == j:
            print("")

# 方法二
print("方法二:\n" + "\n".join(["   ".join(["{}*{} = {}".format(i, j, i*j) for j in range(1, i + 1)]) for i in range(1, 10)]))

print("我是帅气的分割线".center(100, "-"))


# 京牌摇号小程序
"""
需求：
1. 允许⽤户最多选3次
2. 每次放出20个⻋牌供⽤户选择
3. 京[A-Z]-[xxxxx], 可以是数字和字⺟在组合
"""
count = 3  # 用户选择机会
num = 20  # 每次选择提供的车牌号数量
third_letter_sample = string.digits + string.ascii_uppercase  # 第三段车牌字符库

while count > 0:
    car_num_dic = {}
    for i in range(num):
        second_letter = random.choice(string.ascii_uppercase)
        third_letter = random.sample(third_letter_sample, 5)
        car_num = "京" + second_letter + "-" + "".join(third_letter)
        car_num_dic[i] = car_num  # 建立车牌字典
    print(car_num_dic)

    choice = input("请输入您心仪的车牌序号:")
    if choice.isdigit() and int(choice) in range(num):
        print(f"恭喜你选购成功，您的新⻋牌是{car_num_dic[int(choice)]}")
        break
    else:
        count -= 1
        print(f"重新选择，请输入车牌的序号，你还有{count}次机会！")

print("我是帅气的分割线".center(100, "-"))


#  年会抽奖小程序
"""
张三科技有限公司有300员⼯，开年会抽奖，奖项如下：
⼀等奖 3名， 泰国5⽇游
⼆等奖6名，iPhone⼿机
三等奖30名，避孕套⼀盒

规则：
1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
2. 每个员⼯限中奖⼀次，不能重复

"""
# 第一步：生成员工编号列表
num = 300  # 员工数
staff_list = ["员工{}".format(i) for i in range(1, num+1)]

# 第二步：抽奖
bonus_list = [["三等奖", 30], ["二等奖", 6], ["一等奖", 3]]
for bonus, count in bonus_list:
    winner_list = random.sample(staff_list, count)
    print(f"获得{bonus}的名单为：{winner_list}")
    for each in winner_list:
        staff_list.remove(each)
    print(f"还剩{len(staff_list)}人未得奖！")

