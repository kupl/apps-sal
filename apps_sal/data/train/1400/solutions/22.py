num = []
for i in range(20):
    num.append(2**i)
for _ in range(int(input())):
    n, l, r = list(map(int, input().split()))
    minset = num[:l]
    maxset = num[:r]
    ans1 = 0
    ans2 = 0
    ml = len(minset)
    mal = len(maxset)
    ans1 = sum(minset) + (n - ml) * minset[0]
    ans2 = sum(maxset) + (n - mal) * maxset[-1]

    print(ans1, ans2)
