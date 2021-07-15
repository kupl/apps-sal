def sum_mul(n, m):
    if n>0 and m>0:
       i=1
       ergebnis=0
       
       for i in range (n,m,n):
            ergebnis+=i
       return ergebnis
    else:
       return "INVALID"
