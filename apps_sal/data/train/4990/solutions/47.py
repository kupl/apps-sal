def solution(string, ending):
    print(string[-1 * len(ending): None: 1])
    if ending == '':
        return True
    if ending == string[-1 * len(ending): None: 1]:
        return True
    else:
        return False
