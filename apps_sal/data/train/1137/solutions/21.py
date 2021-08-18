
def check(arr, n):
    s = set()
    for i in range(0, n):
        temp = 2000 - arr[i]
        if (temp in s):
            return("Accepted")
        s.add(arr[i])
    return("Rejected")


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr, n))
