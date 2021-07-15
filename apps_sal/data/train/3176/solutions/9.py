import re
def to_cents(amount):
    pattern = re.compile(r'^\$([\d]+)\.([\d]{2})$')
    if re.fullmatch(pattern, amount) == None:
        return None
    price = re.fullmatch(pattern, amount)
    return (int(price.group(1)) * 100) + int(price.group(2))
