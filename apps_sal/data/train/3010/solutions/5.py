def solution(pairs):
    answer = [str(i) + ' = ' + str(pairs[i]) for i in pairs]
    answer.sort()
    return ','.join(answer)
