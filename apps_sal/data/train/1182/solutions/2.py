t = int(input())
m = [int(input()) for i in range(t)]
print('')
for i in m:
    arr = []
    count = 0
    for a in range(i + 1, i * 2 + 1):
        inpX = i * a / (a - i)
        if inpX >= a and i * a % (a - i) == 0:
            count = count + 1
            arr.append(a)
    print(count)
    for j in arr:
        print(j)
