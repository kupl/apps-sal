def solution(string, ending):
    # your code here...
    end_len=len(ending)
    str_len=len(string)
    actualend=string[str_len-end_len:]
    if actualend==ending:
        return(True)
    else:
        return(False)

