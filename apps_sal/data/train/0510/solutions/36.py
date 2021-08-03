from operator import or_


class SegmentTree:
    def __init__(self, size, op, e):
        self._op = op
        self._e = e
        self._size = size
        t = 1 << (size - 1).bit_length()
        self._offset = t - 1
        self._data = [e] * (t * 2 - 1)

    def __getitem__(self, key):
        return self._data[self._offset + key]

    def __setitem__(self, key, value):
        op = self._op
        data = self._data
        i = self._offset + key
        data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def build(self, iterable):
        op = self._op
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def query(self, start, end):
        op = self._op
        res = self._e
        l = self._offset + start
        r = self._offset + end
        while l < r:
            if l & 1 == 0:
                res = op(res, self._data[l])
            if r & 1 == 0:
                res = op(res, self._data[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res


def str2bit(c):
    return 1 << (ord(c) - ord('a'))


N = int(input())
S = input()

st = SegmentTree(N, or_, 0)
st.build(str2bit(x) for x in S)

M = int(input())
for i in range(M):
    q, a, b = input().split()
    if q == "1":
        st[int(a) - 1] = str2bit(b)
    elif q == "2":
        print(bin(st.query(int(a) - 1, int(b))).count("1"))
