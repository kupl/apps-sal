for _ in range(int(input())):
    n = int(input())
    s = input()
    total = 0
    zero = s.count('0')
    one = s.count('1')
    for i in range(n):
        if s[i] == '0':
            zero -= 1
            total += one
        else:
            one -= 1
            total += zero
    print(total)
