s = input()

n = len(s)
ans = [0] * n
left = n - 1
right = 0
if (s[0] == "l"):
    ans[n - 1] = 1
    left -= 1
else:
    ans[0] = 1
    right += 1
for i in range(1, n):
    if (s[i] == "l"):
        ans[left] = i + 1
        left -= 1
    else:
        ans[right] = i + 1
        right += 1
for num in ans:
    print(num)
