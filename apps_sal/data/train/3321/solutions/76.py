def evil(n):
    s = []                        # List reminder
    length = (n+2) // 2
    for i in range(length):
        r = n % 2
        s.append(r)
        if n // 2 == 0:
            break
        n = n//2
    
    s_reverse = s[::-1]           # reverse list
    binary = ""                   # conversion to string
    for n in s_reverse:
        binary += str(n)
    
    count = 0                    # Ones count
    for s in binary:
        if s == "1":
            count += 1
        
    if count % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
