for _ in range(int(input())):
    n = int(input())
    s = input().split(' ')
    a = set()
    for i in range(n):
        a.add(eval(s[i]))
    print(len(a))
