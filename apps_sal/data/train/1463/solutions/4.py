from itertools import combinations

try:
    for _ in range(int(input())):
        def __gcd(a, b):
            if a == 0 or b == 0:
                return 0
            if a == b:
                return a
            if a > b:
                return __gcd(a - b, b)
            return __gcd(a, b - a)

        def areNocoprime(arr):
            if __gcd(arr[0], arr[1]) == 1:
                return True
            else:
                return False

        def iscoprime(arr):
            arr2 = list(combinations(arr, 2))
            arr3 = [areNocoprime(i) for i in arr2]
            if False in arr3:
                return False
            return True

        def isarraycoprime(arr, n):
            arr2 = []
            arr2.extend(arr)
            arr2.append(n)
            if iscoprime(arr2) is True:
                return arr2
            else:
                return arr

        sum = 0
        n = int(input())
        pages = [i for i in range(1, n + 1)]
        big_arr = []
        small_arr = []
        summ = 0
        while pages.count(0) != n:
            for i in range(0, n):
                if pages[i] != 0:
                    x = len(small_arr)
                    small_arr = isarraycoprime(small_arr, pages[i])
                    y = len(small_arr)
                    if x != y:
                        pages[i] = 0
            big_arr.append(small_arr)
            small_arr = []
        print(len(big_arr))
        for i in big_arr:
            print(len(i), *i)

except EOFError as e:
    print(end=" ")
