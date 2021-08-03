# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr1 = set(arr)
    dif = n - len(arr1)
    print(n - dif - (dif % 2))
