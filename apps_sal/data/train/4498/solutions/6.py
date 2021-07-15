def solution(roman):
    ans = 0
    numerals = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    for x in range(0,len(roman)):
        if x < len(roman)-1 and numerals[roman[x]] < numerals[roman[x+1]]:
            ans = ans - numerals[roman[x]]
        else:
            ans = ans + numerals[roman[x]]
    return ans
