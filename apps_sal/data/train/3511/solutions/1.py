def find_key(enc):
    n = int(enc,16)
    for i in range(2,int(n**.5)+1):
        if not n%i:
            return (i-1)*(n//i-1)

