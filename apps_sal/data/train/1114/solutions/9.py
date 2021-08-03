def main():
    t = int(input())
    while(t != 0):
        n = int(input())
        arr = list(map(int, input().split()))
        maxVal = -1
        for i in range(0, n):
            for j in range(i + 1, n):
                temp = arr[i] + arr[j]
                if(maxVal < temp):
                    maxVal = temp

        count = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                temp = arr[i] + arr[j]
                if(maxVal == temp):
                    count += 1
        val = (n * (n - 1)) / 2
        print(count / val)
        t = t - 1


def __starting_point():
    main()


__starting_point()
