def jumping_number(n):
    if n < 10: return 'Jumping!!'
    n = str(n)
    return 'Jumping!!' if all( abs(int(n[i])-int(n[i+1]) )==1 for i in range(len(n) - 1) ) else 'Not!!'
