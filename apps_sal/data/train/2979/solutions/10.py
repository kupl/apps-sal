def get_age(age):
    return int(__import__('re').search(r'\d+', age).group(0))
