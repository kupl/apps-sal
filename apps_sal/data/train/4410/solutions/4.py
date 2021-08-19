def count_sixes(n):
    res = str(10 ** n // 15 - (-5) ** n // 15)
    return len(res) - len(res.lstrip('6'))


" For my poor memory :\n\n    with some paper and a pen, 2->10:\n        2 : 0.5\n        3 : 0.75\n        4 : 0.625\n        5 : 0.6875\n        6 : 0.65625\n        7 : 0.671875\n        8 : 0.6640625\n        9 : 0.66796875\n        10 : 0.666015625 ==> that's the example !\n        \n    I'm lazy : check OEIS with only the decimals (5, 75, 625, 6875...) ==> https://oeis.org/A091903\n    Formula : a(n)=10^n/15-(-5)^n/15\n    \n    Adapt formula to python :)\n"
