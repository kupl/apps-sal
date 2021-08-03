def solution(string, ending):
    if ending == "" or string[-int(len(ending)):] == ending:
        return True
    else:
        return False
