t = int(input())
for _ in range(t):
    s = input().strip()
    n = int(input())
    chars = set(input().split())
    flag = 1
    for i in s:
        if i not in chars:
            print(0)
            flag = 0
            break
    if flag:
        print(1)
