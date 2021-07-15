def count(a):
    n   = len(a)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                cnt+=1
    return cnt          

n = int(input())
p = list(map(int, input().split()))
num = count(p)

print(num*2 - num%2)
