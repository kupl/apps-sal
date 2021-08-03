t = eval(input())
for w in range(t):
    n = eval(input())
    lst = list(map(int, input().split()))
    total = sum(lst)
    left = 0
    k = 0
    for i in range(n):
        right = total - lst[i] - left
        if(right == left):
            print(i)
            k = 1
            break
        left = left + lst[i]
    if(k == 0):
        print('-1')
