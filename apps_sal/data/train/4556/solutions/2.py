def count_me(s):
    return __import__('re').sub('(\\d)\\1*', lambda x: f'{len(x.group())}{x.group(1)}', s) * s.isdigit()
