for _ in range(int(input())):
    s = int(input())
    rev = 0
    while(s > 0):
        rev = rev * 10 + s % 10
        s = s // 10
    print(rev)
