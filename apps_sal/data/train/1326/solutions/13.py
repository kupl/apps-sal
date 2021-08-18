for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    curr_fuel = arr[0]
    count = 0
    if arr[0] != 0:
        for i in range(1, n):
            curr_fuel -= 1
            curr_fuel += arr[i]
            count += 1
            if curr_fuel == 0:
                break
        count += curr_fuel

    print(count)
