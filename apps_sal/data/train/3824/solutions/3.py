def find_spec_partition(n, k, com):
    if com == 'min':
        answer = [n]
        while len(answer) != k:
            answer[0] -= 1
            answer.append(1)
        return answer
    else:
        answer = [1 for i in range(k)]
        cur = 0
        while sum(answer) != n:
            answer[cur] += 1
            cur += 1
            if cur == k:
                cur = 0
        return answer
