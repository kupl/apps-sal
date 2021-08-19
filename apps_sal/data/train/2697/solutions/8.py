def solution(s):
    fCam = [i for i in range(len(s) - 1) if all((s[i].islower(), s[i + 1].isupper()))]
    return ''.join([[e, f'{e} '][i in fCam] for (i, e) in enumerate(s)])
