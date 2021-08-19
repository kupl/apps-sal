names = input().split()
n = int(input())
print(' '.join(names))
for i in range(n):
    (died, new) = input().split()
    if died == names[0]:
        names = [new, names[1]]
    else:
        names = [names[0], new]
    print(' '.join(names))
