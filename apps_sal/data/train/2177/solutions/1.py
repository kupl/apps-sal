def main():
    input()
    numbers = tuple(map(int, input().split()))
    d = []
    for i in range(len(numbers)):
        while len(d) <= numbers[i]:
            d.append([])
        d[numbers[i]].append(i)
    dd = [[]]
    for line in d:
        if line:
            dd.append(line)
    d = dd
    answer = [None] * len(numbers)
    for item in d[1]:
        answer[item] = 1
    for i in range(1, len(d) - 1):
        left_maxes = [0]
        right_maxes = [0]
        for j in range(len(d[i])):
            left_maxes.append(max(left_maxes[-1], answer[d[i][j]]))
            right_maxes.append(max(right_maxes[-1], answer[d[i][len(d[i]) - j - 1]]))
        left_amount = 0
        for j in range(len(d[i + 1])):
            while left_amount < len(d[i]) and d[i][left_amount] < d[i + 1][j]:
                left_amount += 1
            answer[d[i + 1][j]] = max(left_maxes[left_amount], right_maxes[len(d[i]) - left_amount] + 1)
    res = 0
    for ans in answer:
        res += ans
    print(res)


def __starting_point():
    main()


__starting_point()
