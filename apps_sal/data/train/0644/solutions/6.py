for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    sums = sum(array)
    if sums // n == sums / n:
        print("Yes")
    else:
        print("No")
