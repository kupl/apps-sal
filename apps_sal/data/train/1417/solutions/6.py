for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_c = [arr.count(i) for i in range(1, 9)]
    print(min(arr_c))
