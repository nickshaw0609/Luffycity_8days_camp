import re

f = open("stocks.txt", encoding='utf-8')
headers = f.readline().strip().split(",")  # 表头
stock_dic = {}
"""
'传艺科技'  :  [ '2866', '传艺科技', '13.81', '10.04%', '1.26', '13.59万', '1.83亿', '9.72%', '13.81', '12.59', 
'12.61', '12.55', '2.63', '16.86%', '33.37', '3.43']
"""

for line in f:
    line = line.strip().split(",")
    stock_dic[line[1]] = line

# 模糊查询
while True:
    cmd = input("请输入您要查询的股票：").replace(" ", "")
    print(headers)
    if not cmd:
        continue
    match_count = 0
    for st_name, info in stock_dic.items():
        if cmd in st_name:
            print(info)
            match_count += 1
    syntax_format_list = re.split("[<>]", cmd)
    if len(syntax_format_list) == 2:
        try:  # 用户输入值可能出现格式错误
            input_column, input_value = syntax_format_list
            if input_column in headers:
                input_value = float(input_value)
                column_index = headers.index(input_column)
                for st_name, info in stock_dic.items():
                    true_value = float(info[column_index].strip("%"))
                    if "<" in cmd:
                        if true_value < input_value:
                            print(info)
                            match_count += 1
                    if ">" in cmd:
                        if true_value > input_value:
                            print(info)
                            match_count += 1
        except ValueError as e:
            print("输入值格式错误！", e)
    print(f"\033[1;34;1m匹配到了{match_count}数据.\033[0m")  # 颜色打印格式：\033[显示方式;前景色;背景色m要打印的文字\033[0m

