import time

def f(m):
    print('第{}次被调用！'.format(m))


def scheduler(f, n, m):
    a = m
    while m > 0:
        time.sleep(n/1000.0)
        m -= 1
        f(a - m)

scheduler(f, 800, 10)
