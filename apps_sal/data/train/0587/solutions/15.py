n = int(input())
arr = list(map(int, input().split()))
for x in arr:
    if x == 2:
        print(end='1 ')
    else:
        y = x % 4
        if y > 1:
            print(x - 2, end=' ')
        else:
            print(x + 2, end=' ')
print()
