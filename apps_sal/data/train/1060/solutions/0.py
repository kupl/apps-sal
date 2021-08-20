def countSubstr(str, n, x, y):
    tot_count = 0
    count_x = 0
    for i in range(n):
        if str[i] == x:
            count_x += 1
        if str[i] == y:
            tot_count += count_x
    return tot_count


t = int(input())
for _ in range(t):
    n = int(input())
    str = input()
    x = '0'
    y = '1'
    x1 = '1'
    y1 = '0'
    c1 = countSubstr(str, n, x, y)
    c2 = countSubstr(str, n, x1, y1)
    print(c1 + c2)
