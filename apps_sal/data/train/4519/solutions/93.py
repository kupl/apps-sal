def max_number(n):
    lst = [int(i) for i in str(n)]
    lst.sort(reverse = True)
    s = [str(i) for i in lst] 
    fin = int("".join(s))
    return fin
  

