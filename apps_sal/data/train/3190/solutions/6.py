p = '11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97'.split()
li = [i for i in range(1,1000000) if str(i)[:2] in p and str(i*i)[:2] in p and str(i*i)[-2:]==str(i)[-2:]]
solve=lambda a,b:sum(1 for i in li if a<=i<=b)
