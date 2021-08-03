s = input()
mod = 1000000007
step = 0
p = 1

for x in s:
    if x == 'a':
        p = (p * 2) % mod
    else:
        step = (step + p - 1) % mod

print(step)
