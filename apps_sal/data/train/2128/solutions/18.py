#! usr/bin/env python3
# coding:UTF-8

# wdnmd UKE
# wcnm UKE
# wrnnn UKE

ans = 0
cnt = 0
N = input()
t = input().split()

for i in t:
    if(int(i) == 1):
        cnt += 1
    else:
        ans += cnt

print(ans)

