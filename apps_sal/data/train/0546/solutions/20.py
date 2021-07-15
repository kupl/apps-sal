for _ in range(int(input())):
    a=int(input())
    b=list(bin(a))
    print(b.count('1')-1)

