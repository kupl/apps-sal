# cook your code here
# cook your code here
pow2 = [(1 << i) for i in range(21)]


for t in range(eval(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    cnt = 0
    for i in range(k):
        if pow2[i] not in l:
            cnt += 1
    print(cnt)
