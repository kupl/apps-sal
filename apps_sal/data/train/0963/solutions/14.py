for i in range(int(input())):
    n = int(input())
    count = 0
    hill = list(map(int, input().split()))

    def res(hills):
        maxval = max(hills)
        maxpos = hills.index(maxval)

        left = list()
        right = list()

        if maxpos is 0 or maxpos is len(hills) - 1:
            return 1

        for j in range(maxpos):
            left.append(hills[j])
        for j in range(maxpos + 1, len(hills)):
            right.append(hills[j])

        return 1 + min(res(right), res(left))

    print(res(hill))
