def solution(a, b):
    zA = []
    for iA in a:
        zA.append(len(iA))
    zB = []
    for iB in b:
        zB.append(len(iB))
    if zA < zB:
        return f"{a+b+a}"
    else:
        return f"{b+a+b}"
