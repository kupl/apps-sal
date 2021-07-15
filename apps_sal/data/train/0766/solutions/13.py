# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    list_n = list(map(int, input().split()))
    list_n = sorted(list_n)
    print(list_n[-1]*list_n[-2], list_n[0]*list_n[1])
    t-=1
