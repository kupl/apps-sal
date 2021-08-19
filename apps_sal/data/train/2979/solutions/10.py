def get_age(age):
    return int(__import__('re').search('\\d+', age).group(0))
