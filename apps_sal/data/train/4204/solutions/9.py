""" Solution without loops ! """
' Define the first segment of what wwould be a "not far away palindrome" based on "num" :\n            num = 1258  -> midPart = 12  ( -> would give "1221" )\n            num = 459   -> midPart = 45  ( -> would give "454"  )\n    \n    Check for lower and upper values (in case num is near of change of decade, upperbond or lowerbond)\n    and define 3 possible parts of palindromes:\n            num = 1258  -> 12  ->  lowPart  = 11\n                                   midPart  = 12\n                                   highPart = 13\n            num = 459   -> 45  ->  lowPart  = 44\n                                   midPart  = 45\n                                   highPart = 46\n                                   \n    Construct palindromes according to each part an the parity of the length of the original number:\n            num = 1258  -> lPal = 1111 ; mPal = 1221 ; hPal = 1331\n            num = 459   -> lPal = 444  ; mPal = 454  ; hPal = 464\n    \n    Sort the result with tuples defined as:     (abs(num-newPal), -newPal)\n    This way, the nearest new palindrome value are first, and if two values of "abs(num-newPal)"\n    are equal, the second element of the tuple ensure to find the highest one as first element of \n    the sorted list of tuples.\n    return the opposite of the second element of the first tuple, which is so "newPal".\n    \n    Edge cases:  num = 1999 -> lPal = 1881 ; mPal = 1991 ; hPal = 2002  =>  return 2002\n                 num = 801  -> lPal = 797  ; mPal = 808  ; hPal = 818   =>  return 797\n                 num = 1002 -> lPal = 99(!); mPal = 1001 ; hPal = 1111  =>  return 1001\n'


def nextPal(sPart, ls):
    return int(sPart + sPart[:len(sPart) - ls % 2][::-1])


def palindrome(num):
    if type(num) != int or num <= 0:
        return 'Not valid'
    s = str(num)
    midPart = s[:(len(s) + 1) // 2]
    lowPart = str(int(midPart) - 1)
    highPart = str(int(midPart) + 1)
    (lPal, mPal, hPal) = (nextPal(lowPart, len(s)), nextPal(midPart, len(s)), nextPal(highPart, len(s)))
    return 11 if num <= 16 else -sorted(((abs(num - pal), -pal) for pal in [lPal, mPal, hPal]))[0][1]
