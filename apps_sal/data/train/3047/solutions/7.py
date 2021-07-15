from re import sub; repeating_fractions=lambda n,d: (lambda div: (lambda index: div[:index]+sub(r"(\d)\1+","(\g<1>)",div[index:]))(div.index(".")))(str(1.0*n/d))
