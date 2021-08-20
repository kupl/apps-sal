from sys import stdin
mod = 1000000007
for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    ans = 1
    for ele in s:
        if ele == '7' or ele == '9':
            ans = ans * 4 % mod
        else:
            ans = ans * 3 % mod
    print(ans % mod)
