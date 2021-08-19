# cook your dish here
test = int(input())

for _ in range(test):

    flag = 0
    N = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        if i % 2 == 0:
            print("NO")
            flag = 1
            break

    if flag == 0:
        print("YES")
