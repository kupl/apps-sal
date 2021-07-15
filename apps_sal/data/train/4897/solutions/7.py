def check(n):                   #求所有除数之和
    set1 = set()    #创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            set1.add(i)
            set1.add(n//i)
    return set1

def binary_gcd(x, y):
    if x==0 and y==0:
        return 0
    elif x == 0 and y !=0:
        a = y
    elif y == 0 and x !=0:
        a = x
    else:
        a = max(check(abs(x)) & check(abs(y)))

    num = 0
    while a != 0:
        a = a & (a - 1) # 就是这个操作，需要掌握，它的本质含义是抹去了0不考虑
        num += 1

    return num
