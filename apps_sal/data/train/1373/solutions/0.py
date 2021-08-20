def main():
    t = int(input())
    while t != 0:
        (n, k) = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        freq = [0] * 100001
        k = k - 1
        st = 0
        end = 0
        currentCount = 0
        previousElement = 0
        for i in range(n):
            freq[arr[i]] += 1
            if freq[arr[i]] == 1:
                currentCount += 1
            while currentCount > k:
                freq[arr[previousElement]] -= 1
                if freq[arr[previousElement]] == 0:
                    currentCount -= 1
                previousElement += 1
            if i - previousElement + 1 >= end - st + 1:
                end = i
                st = previousElement
        print(end - st + 1)
        t = t - 1


def __starting_point():
    main()


__starting_point()
