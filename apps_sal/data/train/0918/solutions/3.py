# cook your dish here

for t in range(int(input())):
    n = int(input())
    ans = ((1 << n) - 1) if n < 33 else ((1 << 33) - 1)
    print("Case {}: {}".format(t + 1, ans))
