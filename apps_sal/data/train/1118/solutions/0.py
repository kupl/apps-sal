"""
Name : Jaymeet Mehta
codechef id :mj_13
Problem : Avenir Strings
"""
from sys import stdin, stdout
test = int(stdin.readline())
for _ in range(test):
    N = int(stdin.readline())
    seq = list(input())
    (fp, fp1, fl, fl1) = (0, 0, 0, 1)
    for i in range(N):
        if fl != int(seq[i]) - 0:
            fp += 1
        fl = 1 - fl
    for i in range(N):
        if fl1 != int(seq[i]) - 0:
            fp1 += 1
        fl1 = 1 - fl1
    print(fp) if fp < fp1 else print(fp1)
