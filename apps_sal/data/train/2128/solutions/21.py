#! usr/bin/env python3
# coding:UTF-8

# wdnmd UKE
# wcnm UKE
# wrnnn UKE
# UKE 5
# UKE 6
# UKE 7

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

