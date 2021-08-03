from operator import or_


class SegmentTree():
    """A segment Tree.

    This is a segment tree without recursions.
    This can support queries as follows:
     - update a single value in O(logN).
     - get the folded value of values in a segment [l, r) in O(logN)
    N is the length of the given iterable value.

    Parameters
    ----------
    iterable : Iterable[_T]
        An iterable value which will be converted into a segment tree
    func : Callable[[_T, _T], _T]
        A binary function which returns the same type as given two.
        This has to satisfy the associative law:
            func(a, func(b, c)) = func(func(a, b), c)
    e : _T
        The identity element of the given func.
        In other words, this satisfies:
            func(x, e) = func(e, x) = x
    """

    def __init__(self, iterable, func, e):
        self.func = func
        self.e = e

        ls = list(iterable)
        self.n = 1 << len(ls).bit_length()
        ls.extend([self.e] * (self.n - len(ls)))

        self.data = [self.e] * self.n + ls
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.func(self.data[2 * i], self.data[2 * i + 1])

    def replace(self, index, value):
        """replace the old value of the given index with the given new value.

        This replaces the old value of the given index with the given new value in O(logN).
        This is like "list[index] = value".

        Parameters
        ----------
        index : int
            The index of the value which will be replaced.
        value : _T
            The new value with which the old value will be replaced.
        """
        index += self.n
        self.data[index] = value
        index //= 2
        while index > 0:
            self.data[index] = self.func(self.data[2 * index], self.data[2 * index + 1])
            index //= 2

    def folded(self, l, r):
        """get the folded value of values in a segment [l, r).

        This get the folded value of values in a segment [l, r) in O(logN).
        If func is add, it returns the sum of values in [l, r).
        In other words, this is eqivalent to "sum(list[l:r])".
        If func is other functions, then this is equivalent to "accumulate(list[l:r], func)".

        Parameters
        ----------
        l : int
            The left edge.
        r : int
            The right edge.

        Returns
        -------
        _T(the same type as the type of the element of the given iterable)
            This is equivalent to func(list[l], func(list[l+1], ... ) ).
            If func is represented as '*', then it's:
            list[l] * list[l+1] * ... * list[r-1] 
        """

        left_folded = self.e
        right_folded = self.e
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                left_folded = self.func(left_folded, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.func(self.data[r], right_folded)
            l //= 2
            r //= 2

        return self.func(left_folded, right_folded)


N = int(input())
S = input()

ls = [1 << (ord(c) - ord('a')) for c in S]
segtree = SegmentTree(ls, or_, 0)

Q = int(input())
for _ in range(Q):
    s = input()
    if s[0] == '1':
        i, c = s[2:].split()
        segtree.replace(int(i) - 1, 1 << (ord(c) - ord('a')))
    else:
        l, r = list(map(int, s[2:].split()))
        value = segtree.folded(l - 1, r)
        print((format(value, 'b').count('1')))
