def spin_solve(sentence):
    nu_list=[]
    words = sentence[:-1].split()
    for x in words:
        if x.endswith(',') and len(x) > 7:
            x=x[:-1]
            nu_list.append(f"{x[::-1]},")
        elif x.endswith(',') and len(x) <= 7 or len(x) == 2:
            nu_list.append(x.upper())     
        elif len(x) > 6 or x.count('t') >= 2:
            nu_list.append(x[::-1])
        elif len(x) == 1:
            nu_list.append('0')
        elif len(x) ==3 or len(x) <= 6:
            nu_list.append(x)
    return f"{' '.join(nu_list)}."
