from collections import Counter
t = int(input())
ANS = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = sorted(list(dict(Counter(a)).values()), reverse=True)
    i = 1
    ans = freq[0]
    last = freq[0]
    while i < len(freq):
        val = freq[i]
        if val >= last:
            val = last - 1
        if(val <= 0):
            break
        else:
            ans += val
            i += 1
            last = val
    ANS.append(ans)
for i in ANS:
    print(i)
