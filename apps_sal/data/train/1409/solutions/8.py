for _ in range(int(input())):
    n=int(input())
    s=bin(n)
    s=s[2:]
    print(s.count('1'))
