import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    cnts = [0] * 40
    for i in range(n):
        for j in range(40):
            if (a[i] >> j) & 1:
                cnts[j] += 1

    for cnt in cnts[::-1]:
        cnt0 = n - cnt
        cnt1 = cnt
        if cnt1 % 2 == 0:
            continue
        if cnt1 % 4 == 1:
            print("WIN")
            break
        if cnt1 % 4 == 3 and cnt0 % 2 == 1:
            print("WIN")
            break
        if cnt1 % 4 == 3 and cnt0 % 2 == 0:
            print("LOSE")
            break
    else:
        print("DRAW")
