def reverse_bits(n):
    listbin = [bin(n)]
    listbin.sort(reverse=True)
    pleasework = list(''.join(listbin))
    comeonguy = ''.join(pleasework)
    almostanswer = comeonguy[:1:-1]
    answer = int(almostanswer, 2)
    return answer

    pass
