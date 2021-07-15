def swapping(fir, sec):
    sf = set(fir)
    for ch in sf:
        occurs = fir.count(ch)
        if occurs%2 != 0 and ch in sec.lower():
          f =f"{ch}{ch.upper()}"
          s =f"{ch.upper()}{ch}" 
          t = sec.maketrans(f, s)
          sec = sec.translate(t)
    return sec

def work_on_strings(a,b):
    return swapping(b.lower(),a)+ swapping(a.lower(),b)
