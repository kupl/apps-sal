def complete_binary_tree(a):
    def calculate(a, root=1, cnt=0, output=[]):
        idx = list(range(1, len(a) + 1))
        if (not output):
            output = [0] * len(a)

        if (root * 2 in idx):
            cnt, output = calculate(a, root=root * 2, cnt=cnt, output=output)

        output[root - 1] = a[cnt]
        cnt += 1

        if (root * 2 + 1 in idx):
            cnt, output = calculate(a, root=root * 2 + 1, cnt=cnt, output=output)

        return cnt, output
    return calculate(a)[1]
