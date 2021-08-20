for i in range(int(input())):
    n = int(input())
    rev_num = 0
    while n > 0:
        a = n % 10
        rev_num = rev_num * 10 + a
        n = n // 10
    print(rev_num)
