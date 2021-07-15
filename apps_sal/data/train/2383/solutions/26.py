# We are evolved to search for meaning but ultimately life has none. Naval Ravikant
# by : Blue Edge - Create some chaos

for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    s=max(max(a,b),2*min(a,b))
    print(s*s)

