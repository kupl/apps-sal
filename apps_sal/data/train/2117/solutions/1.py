import math
import random


class AVLTree():
    def __init__(self, x):
        self.left = None
        self.rght = None
        self.val = x
        self.height = 1


def getHeight0(root):
    if root == None:
        return 0
    return max(getHeight0(root.left), getHeight0(root.rght)) + 1


def getHeight(root):
    if root == None:
        return 0
    return root.height


def insert(root, x):
    if root == None:
        return AVLTree(x)
    if x == root.val:
        return root
    if x < root.val:
        root.left = insert(root.left, x)
    elif x > root.val:
        root.rght = insert(root.rght, x)
    hl = getHeight(root.left)
    hr = getHeight(root.rght)
    root.height = max(hl, hr) + 1

    if hr - hl > 1:
        assert hr - hl == 2
        hrr = getHeight(root.rght.rght)
        hrl = getHeight(root.rght.left)
        if hrr == hrl + 1:
            new_root = root.rght
            root.rght = new_root.left
            new_root.left = root
            root.height -= 2
            return new_root
        elif hrl == hrr + 1:
            new_root = root.rght.left
            root.rght.left = new_root.rght
            new_root.rght = root.rght
            root.rght = new_root.left
            new_root.left = root
            root.height -= 2
            new_root.height += 1
            new_root.rght.height -= 1
            return new_root
        else:
            assert False
    elif hl - hr > 1:
        assert hl - hr == 2
        hlr = getHeight(root.left.rght)
        hll = getHeight(root.left.left)
        if hll == hlr + 1:
            new_root = root.left
            root.left = new_root.rght
            new_root.rght = root
            root.height -= 2
            return new_root
        elif hlr == hll + 1:
            new_root = root.left.rght
            root.left.rght = new_root.left
            new_root.left = root.left
            root.left = new_root.rght
            new_root.rght = root
            root.height -= 2
            new_root.height += 1
            new_root.left.height -= 1
            return new_root
        else:
            assert False
    return root


def findUpperBound(root, x):
    if root == None:
        return None
    if x >= root.val:
        return findUpperBound(root.rght, x)
    tmp_bound = findUpperBound(root.left, x)
    if tmp_bound == None:
        return root.val
    return tmp_bound


def findLowerBound(root, x):
    if root == None:
        return None
    if x <= root.val:
        return findLowerBound(root.left, x)
    tmp_bound = findLowerBound(root.rght, x)
    if tmp_bound == None:
        return root.val
    return tmp_bound


def inorder(root):
    if root == None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.rght)


def checkHeight(root):
    if root == None:
        return True
    if not checkHeight(root.left):
        return False
    if not checkHeight(root.rght):
        return False
    return abs(getHeight0(root.left) - getHeight0(root.rght)) <= 1


def testAVL():
    l = [x for x in range(100)]
    for i in range(100):
        ni = random.randint(0, 99)
        l[i], l[ni] = l[ni], l[i]

    tree = None
    for v in l:
        tree = insert(tree, v)
    assert inorder(tree) == [i for i in range(100)]
    assert checkHeight(tree) == True


class HeapObj():
    def __init__(self, v, n):
        self.val = v
        self.hpidx = n


def shiftup(n, r, hp):
    while r >= 0:
        j = r * 2 + 1
        if j < n:
            if j + 1 < n and hp[j + 1].val > hp[j].val:
                j += 1
            if hp[j].val <= hp[r].val:
                return
            hp[r], hp[j] = hp[j], hp[r]
            hp[r].hpidx = r
            hp[j].hpidx = j
        if r == 0:
            break
        r = int((r - 1) / 2)


def shiftdown(n, r, hp):
    while r < n:
        j = r * 2 + 1
        if j >= n:
            return
        if j + 1 < n and hp[j + 1].val > hp[j].val:
            j += 1
        if hp[j].val <= hp[r].val:
            return
        hp[r], hp[j] = hp[j], hp[r]
        hp[r].hpidx = r
        hp[j].hpidx = j
        r = j


def testHeap():
    hp = []
    for _ in range(100):
        obj = HeapObj(random.randint(0, 9999), len(hp))
        hp.append(obj)
        shiftup(len(hp), len(hp) - 1, hp)
    res = []
    while hp:
        res.append(hp[0].val)
        hp[0], hp[-1] = hp[-1], hp[0]
        hp[0].hpidx = 0
        hp.pop()
        shiftdown(len(hp), 0, hp)
    assert res == sorted(res, reverse=True)


def calc(n, a):
    ia = [x for x in enumerate(a)]
    ia.sort(key=lambda tp: tp[1])
    tree = None
    tree = insert(tree, -1)
    tree = insert(tree, n)

    hpobj = HeapObj(n, 0)
    hp = [hpobj]
    itv2hpobj = {(0, n - 1): hpobj}
    ret = []
    nxt = n
    for idx, val in ia:
        interval_end = findUpperBound(tree, idx) - 1
        interval_bgn = findLowerBound(tree, idx) + 1
        itv = (interval_bgn, interval_end)
        assert itv in itv2hpobj
        tree = insert(tree, idx)
        itv2hpobj[itv].val = 2 * n
        hpidx = itv2hpobj[itv].hpidx
        shiftup(len(hp), hpidx, hp)
        hp[0], hp[-1] = hp[-1], hp[0]
        hp[0].hpidx = 0
        hp.pop()
        del itv2hpobj[itv]
        shiftdown(len(hp), 0, hp)

        if idx > interval_bgn:
            new_obj = HeapObj(idx - interval_bgn, len(hp))
            hp.append(new_obj)
            itv2hpobj[(interval_bgn, idx - 1)] = new_obj
            shiftup(len(hp), len(hp) - 1, hp)
        if idx < interval_end:
            new_obj = HeapObj(interval_end - idx, len(hp))
            hp.append(new_obj)
            itv2hpobj[(idx + 1, interval_end)] = new_obj
            shiftup(len(hp), len(hp) - 1, hp)
        NA = 0
        if len(hp) > 0:
            NA = hp[0].val
        while nxt > NA:
            ret.append(val)
            nxt -= 1
    assert len(ret) == n
    ret.reverse()
    return ret


def calc_bf(n, a):
    ans = [None for _ in range(n)]
    for i in range(n):
        minij = None
        for j in range(i, n):
            l = j - i
            if minij == None or minij > a[j]:
                minij = a[j]
            if ans[l] == None or ans[l] < minij:
                ans[l] = minij
    return ans


def duipai():
    n = 10
    a = [random.randint(1, 20) for _ in range(n)]
    res_smt = calc2(n, a)
    res_btf = calc_bf(n, a)
    if res_smt != res_btf:
        print('!')
        print(a)
        print(res_smt)
        print(res_btf)
        return False
    return True


def duipai_n(times):
    for i in range(times):
        print('Att {t}'.format(t=i))
        if not duipai():
            break
        print()


def calc2(n, a):
    ans = [None for _ in range(n)]
    bst_intvs = [None for _ in range(n)]
    stk = [(-1, -2)]
    for idx, v in enumerate(a + [-1]):
        while v <= stk[-1][1]:
            bst_intvs[stk[-1][0]] = idx - stk[-2][0] - 2
            stk.pop()
        stk.append((idx, v))
    for i in range(n):
        iv = bst_intvs[i]
        if ans[iv] == None or ans[iv] < a[i]:
            ans[iv] = a[i]
    for i in range(n - 2, -1, -1):
        if ans[i] == None or ans[i] < ans[i + 1]:
            ans[i] = ans[i + 1]
    return ans


def serious():
    n = int(input())
    a = [int(x) for x in input().split()]
    res = calc2(n, a)
    ans = ''
    for x in res[:-1]:
        ans += str(x) + ' '
    ans += str(res[-1])
    print(ans)


def main():
    serious()


def __starting_point():
    main()


__starting_point()
