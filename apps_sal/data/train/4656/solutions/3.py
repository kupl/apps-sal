from re import sub; center_of=lambda c: sub(r"^(.+?)\1*$","\g<1>","".join((c+c)[(i*(i*2+1)+i)%len(c)] for i in range(len(c))))
