def solution(s):
    result = [i for i in s]
    new = []
    for i in range(0, len(result), 1):
        new.append(result[i:i + 5])

    Lnumber = int(''.join(map(str, max(new))))
    return Lnumber
