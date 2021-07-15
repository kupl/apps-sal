def solution(string, ending):
    for x in range(0,len(string)+1):
        if string[x:len(string)]==ending:
            return True
    return False

