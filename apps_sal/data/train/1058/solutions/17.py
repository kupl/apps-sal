# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    num = input()
    l = [str(int(x) - 2) for x in num]
    ans = "".join(l)
    print(ans)
