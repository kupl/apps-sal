def namelist(names):
    return ', '.join([name['name'] for name in names])[::-1].replace(',', '& ', 1)[::-1]
