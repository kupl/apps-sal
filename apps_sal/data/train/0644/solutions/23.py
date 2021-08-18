
t = input()
for i in range(int(t)):
    n = int(input())
    a = input()
    arr = [int(x) for x in a.split()]
    ans = sum(arr) / n
    if int(ans) == ans:
        print('Yes')
    else:
        print('No')
