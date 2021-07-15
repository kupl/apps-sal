def solution(string, ending):
    # your code here...
    if ending == '':
        return True
    else:
        end_len = -1 * len(ending)    
        return string[end_len:] == ending
