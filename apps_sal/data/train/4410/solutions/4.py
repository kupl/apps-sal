def count_sixes(n):
    res = str(10**n // 15 - (-5)**n // 15)
    return len(res) - len(res.lstrip('6'))


""" For my poor memory :

    with some paper and a pen, 2->10:
        2 : 0.5
        3 : 0.75
        4 : 0.625
        5 : 0.6875
        6 : 0.65625
        7 : 0.671875
        8 : 0.6640625
        9 : 0.66796875
        10 : 0.666015625 ==> that's the example !
        
    I'm lazy : check OEIS with only the decimals (5, 75, 625, 6875...) ==> https://oeis.org/A091903
    Formula : a(n)=10^n/15-(-5)^n/15
    
    Adapt formula to python :)
"""
