n, k = map(int, input().split(' '))
o = n - k
print(1, end=' ')
for i in range(2, o + 1):
    print(i, end=' ')
mb = n
mm = o + 1
while mb >= mm:
    print(mb, end=' ')
    mb -= 1
    if mb >= mm:
        print(mm, end=' ')
        mm += 1
