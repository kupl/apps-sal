"""
        n    t(i)     n-1  (n + i + 1) * (n - i)
s(n) =  Σ   -----  +   Σ   ---------------------
       i=1  i + 1     i=1     2 * (n + i + 1)

        n    i      n-1   n - i
     =  Σ   ---  +   Σ    -----
       i=1   2      i=1     2

        n    i      n-1    i
     =  Σ   ---  +   Σ    ---
       i=1   2      i=1    2

         n      n-1
     =  ---  +   Σ   i
         2      i=1

         n      n * (n - 1)
     =  ---  +  -----------
         2          2

     =  n^2 / 2
"""


def game(n):
    return [n ** 2, 2] if n % 2 else [n ** 2 // 2]
