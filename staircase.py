"""
问题描述：
假设有一个N阶的台阶，设定每一步能走的台阶数存在一个集合中，例如{1, 3, 5}，表示每次能走一阶，三阶或者五阶，求总共有多少中走法。
最好也能输出所有的走法。
"""


# 只得到总共有多少种走法
def get_ways_num(step, current_step):
    global steps, ways_num
    current_step += step
    if current_step == num:
        ways_num += 1
        return
    elif current_step > num:
        return
    else:
        for i in steps:
            get_ways_num(i, current_step)


# 递归解法，并得到所有可能的走法
def get_ways(step, current_step, sets=None):
    global steps, ways_num, possible_sets

    if sets is None:
        sets = []

    current_step += step

    if current_step == num:
        sets.append(step)
        possible_sets.append(sets[1:])
        ways_num += 1
        return True
    elif current_step > num:
        return False
    else:
        sets.append(step)
        for i in steps:
            if get_ways(i, current_step, sets):
                sets.pop()
        sets.pop()


if __name__ == '__main__':
    # 设置台阶的阶数
    num = 10
    # 设置允许一步踏过的阶数
    steps = [1, 3, 5]
    # 所有可能的情况数
    ways_num = 0
    # 所有可能的情况
    possible_sets = []
    # 开始递归
    get_ways(0, 0)
    # 输出结果
    print(ways_num)
    for each_set in possible_sets:
        print(each_set)
