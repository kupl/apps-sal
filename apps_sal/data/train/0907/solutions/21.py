# cook your dish here

def answerFunction(s, n):
    prev = None
    new = ""
    for each in s:
        if each != '.':
            new += each
    if new == "":
        return "Valid"

    if len(new) == 1:
        return "Invalid"

    for i in range(len(new)):  # HTHT
        if i == 0 and new[i] == 'T':
            return "Invalid"
        if new[i] == 'H':
            if prev == 'H':
                return "Invalid"
            else:
                prev = new[i]
        elif new[i] == 'T':
            if prev == 'T':
                return "Invalid"
            else:
                prev = new[i]
    if prev == 'H':
        return "Invalid"
    return "Valid"


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(answerFunction(s, n))
