def seven(m,counter=int()):return seven(m//10-2*int(str(m)[-1]),counter+1) if (m//10-2*int(str(m)[-1]))/100>=1 else ((m//10-2*int(str(m)[-1])),counter+1 if m>=100 else int())

