def check(n):  # 求所有除数之和
    set1 = set()  # 创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            set1.add(i)
            set1.add(n // i)
    return set1


def find_min_num(num_div):  # memoize me, please!
    # your code here
    i = 1
    while 1:
        if len(check(i)) == num_div:
            return i
        i += 1
    return n  # the smallest number in having an amount of divisors equals to numDiv
