n = int(input())
word = input()
cnt = [0] * 26
for x in word:
    cnt[ord(x) - ord('a')] += 1
ind = 25
sum = 0
for i in range(26):
    pre = -1
    cur = -1
    ans = 0
    flag = True
    for (j, x) in enumerate(word):
        if ord(x) - ord('a') < i:
            pre = j
        elif ord(x) - ord('a') == i:
            cur = j
        if j - pre == n:
            if j - cur >= n:
                flag = False
                break
            pre = cur
            ans += 1
    if flag:
        ind = i
        sum = ans
        break
for i in range(ind):
    print(chr(ord('a') + i) * cnt[i], end='')
print(chr(ord('a') + ind) * sum)
