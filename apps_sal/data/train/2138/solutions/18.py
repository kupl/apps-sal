def maxConsecutive(a):
    i = 1
    curr = 0
    if a[0] == '1':
        curr += 1
    ans = curr
    for i in range(len(a)):
        if a[i] == '1':
            curr += 1
        else:
            curr = 1
        ans = max(ans, curr)
    return ans


def countOne(a):
    ans = 0
    for i in range(len(a)):
        if a[i] == '1':
            ans += 1
    return ans


a = input()
b = input()
if countOne(a) + countOne(a) % 2 >= countOne(b):
    print("YES")
else:
    print("NO")

# 101101
#       01111
