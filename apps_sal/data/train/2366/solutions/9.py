def mi():
        return list(map(int, input().split()))
'''
5
6
3 9 4 6 7 5
1
1000000
2
2 1
10
31 41 59 26 53 58 97 93 23 84
7
3 2 1 2 3 4 5
'''
for _ in range(int(input())):
    n = int(input())
    a = list(mi())[::-1]
    m = a[0]
    ans = 0
    for i in range(n):
        if a[i]>m:
            ans+=1
        elif a[i]<m:
            m = a[i]
    print (ans)

