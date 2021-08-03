s = input().split()
n = int(s[0])
k = int(s[1])
tweet = [0] * k
for t in range(k):
    s = input().split()
    if len(s) == 1:
        tweet = [0] * k
        print(0)
        continue
    s = int(s[1])
    if tweet[s - 1] == 1:
        tweet[s - 1] = 0
    else:
        tweet[s - 1] = 1
    ans = 0
    for i in range(k):
        if(tweet[i] == 1):
            ans += 1
    print(ans)
