def solution(string, ending):
    if ending == '':
        return True
    sum = 0
    if len(string) < len(ending):
        return False
    for i in range(1, len(ending) + 1):
        if string[-i] == ending[-i]:
            sum += 1
        else:
            return False
    if sum == len(ending):
        return True
