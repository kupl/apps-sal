n = int(input())
arr = list(map(int, input().split()))
left, right = [-1] * n, [n] * n
ans = [0] * n
st = [0]
for i in range(1, n):
    while st and arr[st[-1]] >= arr[i]:
        st.pop()
    if st:
        left[i] = st[-1]
    st.append(i)
st = [n - 1]
for i in range(n - 2, -1, -1):
    while st and arr[st[-1]] >= arr[i]:
        st.pop()
    if st:
        right[i] = st[-1]
    st.append(i)
for i in range(n):
    ans[right[i] - left[i] - 2] = max(ans[right[i] - left[i] - 2], arr[i])
ans[0] = max(arr)
ans[-1] = min(arr)
for i in range(n - 2, 0, -1):
    ans[i] = max(ans[i], ans[i + 1])
print(" ".join(map(str, ans)))
