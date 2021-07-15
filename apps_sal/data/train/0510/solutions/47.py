class SegmentTree:
    def __init__(self, n, segment_func, identity_element):
        self.n = n
        self.num = 1 << (self.n - 1).bit_length()
        self.segment_func = segment_func
        self.identity_element = identity_element
        self.segment_tree = [self.identity_element] * (2 * self.num)

    def initialize(self, val_arr):
        for i in range(self.n):
            self.segment_tree[self.num + i] = val_arr[i]
        for i in range(self.num - 1, 0, -1):
            self.segment_tree[i] = self.segment_func(self.segment_tree[2 * i], self.segment_tree[2 * i + 1])

    def update(self, idx, val):
        idx += self.num
        self.segment_tree[idx] = val
        while idx > 1:
            self.segment_tree[idx >> 1] = self.segment_func(self.segment_tree[idx], self.segment_tree[idx ^ 1])
            idx >>= 1

    def query(self, left, right):
        res = self.identity_element
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segment_func(res, self.segment_tree[left])
                left += 1
            if right & 1:
                res = self.segment_func(res, self.segment_tree[right - 1])
            left >>= 1
            right >>= 1
        return res

    def bisect_left(self, left, right, target):
        left += self.num
        right += self.num
        left_min = -1
        right_min = -1
        while left < right:
            if left & 1:
                if self.segment_tree[left] >= target and left_min == -1:
                    left_min = left
                left += 1
            if right & 1:
                if self.segment_tree[right - 1] >= target:
                    right_min = right - 1
            left >>= 1
            right >>= 1
        if left_min != -1 or right_min != -1:
            res = left_min if left_min != -1 else right_min
            while res < self.num:
                if self.segment_tree[2 * res] >= target:
                    res *= 2
                else:
                    res *= 2
                    res += 1
            return res - self.num
        else:
            return self.n

    def get_val(self, idx):
        return self.segment_tree[self.num + idx]


def conv_to_int(x):
    return 1 << (ord(x) - ord('a'))


def main():
    n = int(input())
    s = [conv_to_int(t) for t in list(input())]
    q = int(input())
    st = SegmentTree(n, lambda x, y: x | y, 0)
    st.initialize(s)
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            st.update(int(query[1]) - 1, conv_to_int(query[2]))
        else:
            res = st.query(int(query[1]) - 1, int(query[2]))
            ans = 0
            while res:
                ans += res & 1
                res >>= 1
            print(ans)


def __starting_point():
    main()

__starting_point()
