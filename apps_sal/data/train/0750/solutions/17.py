# cook your dish here
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    l1 = [0] * n
    for i in range(n):
        l1[l[i] - 1] = i + 1
    if l == l1:
        print('ambiguous')
    else:
        print('not ambiguous')
