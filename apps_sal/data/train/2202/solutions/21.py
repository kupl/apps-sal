import sys
input = sys.stdin.readline


class SegTree(object):
    """docstring for SegTree"""

    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.tree = [0 for i in range(2 * n)]

    def construct(self):  # Construction
        for i in range(self.n):
            self.tree[n + i] = self.arr[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.function(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        start = index + self.n
        self.tree[start] = value
        while start > 0:
            start = start // 2
            self.tree[start] = self.function(self.tree[2 * start], self.tree[2 * start + 1])

    def calc(self, low, high):  # 0-indexed
        low += self.n
        high += self.n
        ans = 0  # Needs to initialised
        while low < high:
            if low % 2:
                ans = self.function(ans, self.tree[low])
                low += 1
            if high % 2:
                high -= 1
                ans = self.function(ans, self.tree[high])
            low = low // 2
            high = high // 2
        return ans

    def function(self, a, b):  # Function used to construct Segment Tree
        return a + b


def find(num):
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if st.calc(0, mid + 1) > num:
            high = mid - 1
        else:
            low = mid + 1
    if st.calc(0, low + 1) > num:
        return low
    else:
        return low + 1


n = int(input())
a = list(map(int, input().split()))
arr = [i for i in range(1, n + 1)]
st = SegTree(n, arr)
st.construct()
ans = [-1] * n
for i in range(n - 1, -1, -1):
    ind = find(a[i])
    # print (a[i],ind,arr)
    ans[i] = arr[ind]
    st.update(ind, 0)
print(*ans)
