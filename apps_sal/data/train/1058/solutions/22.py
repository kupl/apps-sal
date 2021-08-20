"""
2

3527

47269

3<p<10 :: p>99 and p<10**10
1 ≤ t ≤ 1000
"""
try:
    T = int(input())
    if T >= 1 and T <= 1000:
        for i in range(T):
            num = input()
            if len(num) > 3 and len(num) < 10 ** 10:
                arr = []
                for x in num:
                    arr.append(int(x) - 2)
                arr = list(map(str, arr))
                res = ''.join(arr)
                print(res)
except Exception:
    pass
