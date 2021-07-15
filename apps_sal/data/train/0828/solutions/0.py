for i in range(int(input())):
    a=int(input())
    b=input().split()
    if '0' in b:
        print(100*(a-b.index('0'))+b.count('0')*1000)
    else:
        print(0)

