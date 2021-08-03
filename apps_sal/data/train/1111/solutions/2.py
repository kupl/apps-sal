# cook your dish
for _ in range(int(input())):
    x = int(input())
    arr = list(map(int, input().split()))
    count = 0
    if (x == 1):
        print("0")
    else:
        for i in arr:
            if i % 2 == 0:
                count += 1
        ak = x - count
        print(ak * count)
