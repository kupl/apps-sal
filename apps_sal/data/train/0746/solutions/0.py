def treeProduct(num, h, root, ch):
    if ch >= h:
        return num[root]
    left = root * 2 + 1
    right = root * 2 + 2
    ret1 = treeProduct(num, h, left, ch + 1)
    ret2 = treeProduct(num, h, right, ch + 1)
    return num[root] * max(ret1, ret2)


def main():
    n = int(input())
    while n != 0:
        line = str(input())
        s = line.split()
        num = [int(e) for e in s]
        print(int(treeProduct(num, n, 0, 1) % 1000000007))
        n = int(input())


def __starting_point():
    main()


__starting_point()
