import random
# Exercise 1.8 扎金花


def deliver(player_list):
    """
    发牌器
    :param player_list:输入玩家ID，逗号隔开
    :return: 返回玩家扑克字典
    """
    player_cards_dic = {}
    poker_list = []  # 扑克牌列表
    variety = ["♥", "♦", "♣", "♠"]  # 花色列表
    poker_type = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    for num in poker_type:
        for each in variety:
            poker_list.append([f"{each}{num}", poker_type.index(num) + 2])  # 生成扑克牌

    for each in player_list:
        res = random.sample(poker_list, 3)
        for cards in res:
            poker_list.remove(cards)
        player_cards_dic[each] = res
    return player_cards_dic  # 生成玩家扑克字典


def calc_single(p_cards, score):
    """
    判断单牌
    先排序，加权重，再相加
    :param score: 该玩家手牌得分
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :return:该玩家手牌得分
    """
    weights = [0.1, 1, 10]
    p_cards = sorted(p_cards, key=lambda x: x[1])  # 排序
    for index, i in enumerate(p_cards):
        p_num = i[1]
        score += weights[index] * p_num
    print(f"计算单牌：", p_cards, score)
    return score


def calc_pair(p_cards, score):
    """
    取出牌的数字列表， 集合， 判断长度
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :param score:该玩家手牌得分
    :return:该玩家手牌得分
    """
    card_val_set = {i[1] for i in p_cards}
    if len(card_val_set) < 3:
        score *= 10
    print("计算顺子:", p_cards, score)
    return score


def calc_straight(p_cards, score):
    """
    判断顺子
    :param score: 该玩家手牌得分
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :return:该玩家手牌得分
    """
    p_cards = sorted(p_cards, key=lambda x: x[1])
    a, b, c = [i[1] for i in p_cards]
    if c-b == 1 and b-a == 1:
        score *= 100
    print("计算顺子:", p_cards, score)
    return score


def calc_same_color(p_cards, score):
    """
    同花色判断
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :param score:该玩家手牌得分
    :return:该玩家手牌得分
    """
    color_set = {i[0][0] for i in p_cards}
    if len(color_set) == 1:
        score *= 1000
    print("计算同花", p_cards, score)
    return score


def calc_same_color_straight(p_cards, score):
    """
    同花顺判断
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :param score:该玩家手牌得分
    :return:该玩家手牌得分
    """
    p_cards = sorted(p_cards, key=lambda x: x[1])
    a, b, c = [i[1] for i in p_cards]
    color_set = {i[0][0] for i in p_cards}
    if len(color_set) == 1:
        if c-b == 1 and b-a == 1:
            score *= 10000
    print("计算同花顺:", p_cards, score)
    return score


def calc_leopard(p_cards, score):
    """
    豹子判断
    :param p_cards:单个玩家的手牌列表，例如：[['♥2', 2], ['♠6', 6], ['♠7', 7]]
    :param score:该玩家手牌得分
    :return:该玩家手牌得分
    """
    card_val_set = {i[1] for i in p_cards}
    if len(card_val_set) == 1:
        score *= 100000
    print("计算豹子:", p_cards, score)
    return score


def score_compare(player_card_dic):
    """
    对玩家的手牌进行打分并输出比较结果
    :param player_card_dic: 玩家的手牌，例如：{'1': [['♠7', 7], ['♦A', 14], ['♠9', 9]],}
    :return: 比较大小结果，例如：[['2', 108.3], ['4', 116.5], ['3', 120.7], ['1', 149.7]]
    """
    res_list = []  # 记录游戏结果
    func_list = [
        calc_single,
        calc_pair,
        calc_straight,
        calc_same_color_straight,
        calc_leopard
    ]  # 函数耦合
    for p_name, p_cards in player_cards_dic.items():
        print(f"计算{p_name}的手牌".center(50, "-"))
        score = 0
        for func in func_list:
            score = func(p_cards, score)
        res_list.append([p_name, score])
    res_list = sorted(res_list, key=lambda x: x[1])
    return res_list


players_list = input("请输入玩家姓名，以逗号隔开：").replace(" ", "").split(",")  # 输入玩家ID

player_cards_dic = deliver(players_list)
print("玩家的手牌为：", player_cards_dic)  # 发牌给玩家并生成字典记录玩家牌型

result = score_compare(player_cards_dic)
print(f"游戏结果为：第一名：{result[-1][0]} {result[-1][1]}分，第二名：{result[-2][0]} {result[-2][1]}分，"
      f"第三名：{result[-3][0]} {result[-3][1]}分")  # 游戏结果

#  player_list_sample = ["Nick, Alex, Joker, Batman, God"]
