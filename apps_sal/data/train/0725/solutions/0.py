def magic():

    def check(art, k, m):
        n = len(art)
        for i in range(n - k + 1):
            maxi = 0
            maxi = max(art[i:i + k])
            total = 0
            total = art[i:i + k].count(maxi)
            if total >= m:
                return False
        return True
    for _ in range(eval(input())):
        (n, k, m) = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        dp = []
        ans = 100
        for mask in range(0, 1 << n):
            size = bin(mask).count('1')
            if ans > size:
                art = list(arr)
                for i in range(n):
                    if mask & 1 << i:
                        art[i] += 1
                if check(art, k, m):
                    ans = size
        print(ans if ans != 100 else -1)


magic()
