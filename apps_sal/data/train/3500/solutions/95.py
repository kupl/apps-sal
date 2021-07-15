def remove_exclamation_marks(s):
    new_s=[]
    for n in s:
        if n =="!":
            n=""
        else:
            new_s.append(n)
    answer="".join(new_s)
    return answer
