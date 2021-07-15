from collections import defaultdict
def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

for i in range (int(input())):
    n = int(input())
    layers = defaultdict(int)
    list_ = list(map(int,input().split()))
    for j in range (n):
        layers[list_[j]] += 1
    sum_ = 0
    for j in sorted(layers):
        sum_ += j

    sum_ *= fac(len(layers)-1)
    ans = sum_
    for j in range (len(layers)-1):
        ans = ans*10 + sum_
    print(ans)

    

