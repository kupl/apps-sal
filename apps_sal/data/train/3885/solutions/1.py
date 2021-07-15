def values(n):
    pal = set()
    for i in range(1, int(n**0.5)):
        sos = i*i
        while sos < n:
            i += 1
            sos += i*i
            if str(sos)==str(sos)[::-1] and sos < n:
                pal.add(sos)
    return len(pal)
