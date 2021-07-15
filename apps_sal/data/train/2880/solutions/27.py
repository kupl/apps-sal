seven=lambda m,n=0:len(str(m))>2and seven(int(int(str(m)[:-1])-2*int(str(m)[-1])),-~n)or(m,n)
