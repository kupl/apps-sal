t = int(input())
for i in range(t):
    a = list(input().split())
    b = list(input().split())
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count = count + 1
    if count > 1:
        print('similar')
    else:
        print('dissimilar')
