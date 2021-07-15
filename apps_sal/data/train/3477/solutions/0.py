def sort_string(s, ordering):
    answer = ''
    for o in ordering:
        answer += o * s.count(o)
        s = s.replace(o,'')
    return answer + s 
