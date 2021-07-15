def is_interesting(number, awesome_phrases):
    for i in [number, number+1, number+2]:
        if i<100 :
            continue
        j=str(i)
        if any([
            i in awesome_phrases,
            all([j[x]=='0' for x in range(1,len(j))]),
            all([j[x]==j[0] for x in range(1,len(j))]),
            j == j[::-1],
            j in '1234567890',
            j in '9876543210'
                ]):
            return 2-bool(number-i)
    return 0
