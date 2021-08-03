# cook your dish here
# code
t = int(input())
while(t > 0):
    t -= 1
    n, k = map(int, input().split())
    ans = (n // 2) * (k + 2) + (n % 2) * (2 * k + 1)
    print(ans)
