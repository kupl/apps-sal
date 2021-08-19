def solve(ls):
    result = [ls[each] - ls[each - 1] for each in range(1, len(ls))]
    gap = round(sum(result) / len(result))
    tries = [ls[0] + 1, ls[0], ls[0] - 1]
    answer = []
    while True:
        count = 0
        copy_ls = ls[:]
        copy_ls[0] = tries.pop(0)
        if copy_ls[0] != ls[0]:
            count += 1
        for each in range(len(ls) - 1):
            sub_gap = copy_ls[each + 1] - copy_ls[each]
            if sub_gap < gap:
                copy_ls[each + 1] += 1
                count += 1
            elif sub_gap > gap:
                copy_ls[each + 1] -= 1
                count += 1
        result = [copy_ls[each] - copy_ls[each - 1] for each in range(1, len(ls))]
        if len(set(result)) == 1:
            answer.append(count)
        if len(tries) == 0:
            if len(answer) == 0:
                return -1
            else:
                answer.sort()
                return answer[0]
