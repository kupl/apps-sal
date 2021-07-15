""" Solution without loops ! """

""" Define the first segment of what wwould be a "not far away palindrome" based on "num" :
            num = 1258  -> midPart = 12  ( -> would give "1221" )
            num = 459   -> midPart = 45  ( -> would give "454"  )
    
    Check for lower and upper values (in case num is near of change of decade, upperbond or lowerbond)
    and define 3 possible parts of palindromes:
            num = 1258  -> 12  ->  lowPart  = 11
                                   midPart  = 12
                                   highPart = 13
            num = 459   -> 45  ->  lowPart  = 44
                                   midPart  = 45
                                   highPart = 46
                                   
    Construct palindromes according to each part an the parity of the length of the original number:
            num = 1258  -> lPal = 1111 ; mPal = 1221 ; hPal = 1331
            num = 459   -> lPal = 444  ; mPal = 454  ; hPal = 464
    
    Sort the result with tuples defined as:     (abs(num-newPal), -newPal)
    This way, the nearest new palindrome value are first, and if two values of "abs(num-newPal)"
    are equal, the second element of the tuple ensure to find the highest one as first element of 
    the sorted list of tuples.
    return the opposite of the second element of the first tuple, which is so "newPal".
    
    Edge cases:  num = 1999 -> lPal = 1881 ; mPal = 1991 ; hPal = 2002  =>  return 2002
                 num = 801  -> lPal = 797  ; mPal = 808  ; hPal = 818   =>  return 797
                 num = 1002 -> lPal = 99(!); mPal = 1001 ; hPal = 1111  =>  return 1001
"""

def nextPal(sPart, ls): return int( sPart + sPart[:len(sPart)-ls%2][::-1] )

def palindrome(num):
    if type(num) != int or num <= 0: return "Not valid"
    
    s = str(num)
    midPart  = s[:(len(s)+1)//2]
    lowPart  = str(int(midPart)-1)
    highPart = str(int(midPart)+1)
    lPal, mPal, hPal = nextPal(lowPart, len(s)), nextPal(midPart, len(s)), nextPal(highPart, len(s))
    
    return 11 if num <= 16 else -sorted( (abs(num-pal), -pal)  for pal in [lPal, mPal, hPal] )[0][1]
