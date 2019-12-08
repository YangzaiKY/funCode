import time
import random


if __name__ == '__main__':
    # 设置生成的随机点的数目
    num = 1000000
    
    sum_num = 0
    time_start = time.time()
    for i in range(10):
        points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(num)]
        in_area = lambda point: True if point[0]**2 + point[1]**2 <= 1 else False
        is_in_area = [in_area(point) for point in points]
        in_area_num = is_in_area.count(True)
        sum_num = sum_num + in_area_num
    pi = sum_num / 10 / num *4.0
    time_consume = time.time() - time_start
    print('利用蒙特卡罗方法估算的pi：{:.4f}\n用时{:.2f}s'.format(pi, time_consume))
    input('回车继续...')
