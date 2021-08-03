# cook your dish here
try:

    T = int(input())

    for i in range(T):
        n = int(input())
        s = input()
        arr = [int(i) for i in input().strip().split(" ")]
        res = 1
        result = 0

        for j in range(n - 7):
            res = 1
            res1 = 0
            s1 = s[j:j + 8]
            for i in range(8):
                if s1[i] == 'D':
                    res = res * 2
                    res1 += arr[i]

                elif s1[i] == 'T':
                    res = res * 3
                    res1 = res1 + arr[i]
                elif s1[i] == 'd':
                    res1 = res1 + arr[i] * 2
                elif s1[i] == 't':
                    res1 += arr[i] * 3
                else:
                    res1 += arr[i]
            res = res * res1
            result = max(res, result)
        print(result)
except EOFError:
    pass
