from sys import stdin, stdout
for tc_ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dic = {0: -1}
    ans = last = 0
    for i in range(n):
        last ^= 1 << a[i] - 1
        for j in range(30):
            x = last ^ 1 << j
            if x in dic:
                ans = max(ans, i - dic[x])
        if last not in dic:
            dic[last] = i
    stdout.write(f'{ans >> 1}\n')
