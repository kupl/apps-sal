def solution(string, ending):
    if len(ending) > len(string):
        return False
    if len(ending) == 0:
        return True
    else:
       # try
        ending = ending[::-1]
        string = string[::-1]
        #ll = -1 * len(ending)
        #string = string[ll:]
        for i in range(len(ending)):
            if i > len(string) - 1:
                break
            if ending[i] == string[i]:
                continue
            else:
                return False
        return True
