def commas(n):
    try:
        n = round(n, 3)
    except:
        print('Error')
    res = '{:,}'.format(n)
    print(res)
    if res.endswith('.0'):
        return res[:-2]
    return res
