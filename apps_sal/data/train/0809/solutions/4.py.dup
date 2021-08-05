def checkValidity(a, b, c):

    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
y = len(li)
f = 0
for i in range(y - 2):
    for j in range(i + 1, y - 1):
        a = li[i]
        b = li[j]
        c = li[j + 1]
        if checkValidity(a, b, c):
            x = str(a) + " " + str(b) + " " + str(c)
            print("YES")
            print(x)
            f = 1
            break
    if f == 1:
        break
if f == 0:
    print("NO")
