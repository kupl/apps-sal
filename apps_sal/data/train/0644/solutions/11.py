# cook your dish here
itr = int(input())
while itr:
    itr = itr - 1
    n = int(input())
    inp = [int(n) for n in input().split()]
    ans = "Yes" if sum(inp) % n == 0 else "No"
    print(ans)
