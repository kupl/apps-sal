# cook your dish here
t = int(input())
for _ in range(t):
    n, k, d = list(map(int, input().split()))
    x = list(map(int, input().split()))
    l = list(map(int, input().split()))
    lane = 3 - l[0]
    switched = -float('inf')
    ans = k
    for i in range(n):
     if l[i] == lane:
      if switched + d < x[i] and x[i - 1] + 1 < x[i]:
       lane = 3 - lane
       switched = max(x[i - 1] + 1, switched + d)
      else:
       ans = x[i]
       break
    print(ans)

