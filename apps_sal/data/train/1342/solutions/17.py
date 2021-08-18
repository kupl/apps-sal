T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    my_max = arr[-1]
    if x >= my_max:
        print(len(arr))
    else:
        count = 0
        while x < my_max:
            for i in arr:
                if 2 * i > x and x >= i:
                    arr.remove(i)
                    break
            x *= 2
            count += 1
        print(count + len(arr))
