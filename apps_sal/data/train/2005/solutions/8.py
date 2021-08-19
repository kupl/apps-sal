def get_arr(v):
    ans = []
    while v != 0:
        ans.append(v % 2)
        v //= 2
    return ans[::-1]


def check_arr(arr):
    for i in range(len(arr)):
        for di in range(1, (len(arr) - i) // 2 + 1):
            if i + 2 * di >= len(arr):
                continue
            if arr[i] == arr[i + di] == arr[i + 2 * di]:
                return True
    return False


s = input()
ans = len(s) * (len(s) + 1) // 2
for i in range(len(s)):
    for j in range(i + 1, min(i + 10, len(s) + 1)):
        if not check_arr(s[i:j]):
            ans -= 1
print(ans)
