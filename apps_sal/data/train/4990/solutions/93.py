def solution(string, ending):
    if ending == '': return True
    flag = 0
    i = 0
    for indx in range(len(string) - len(ending), len(string)):
        if string[indx] == ending[i]:
            flag = 1
            i += 1
        else: 
            flag = 0
            break
    if flag == 1: return True
    else: return False
