def year_days(w):
    return f'{w} has 36{5 + (not w % 4 and (not (not w % 100 and w % 400)))} days'
