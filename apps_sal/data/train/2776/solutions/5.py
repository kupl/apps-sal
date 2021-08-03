def commas(num):
    number = float(num)
    return f'{number:,.0f}' if number.is_integer() else f'{number:,.3f}'.rstrip('0').rstrip('.')
