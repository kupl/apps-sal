from sys import stdin
input = stdin.readline
n = int(input())
arr, cnt, curr_len, curr_sum = [0] * (n + 1), [0] * (n + 1), 1, 0
for _ in range(n):
    s = input()
    if s[0] == '1':
        _, x, y = list(map(int, s.split()))
        curr_sum += x * y
        cnt[x - 1] += y
    elif s[0] == '2':
        _, x = list(map(int, s.split()))
        curr_sum += x
        arr[curr_len] = x
        curr_len += 1
    else:
        curr_len -= 1
        curr_sum -= arr[curr_len] + cnt[curr_len]
        cnt[curr_len - 1] += cnt[curr_len]
        cnt[curr_len] = 0
    print('%.9f' % (curr_sum / curr_len))
