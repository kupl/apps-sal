format_poem = __import__('functools').partial(__import__('re').sub, '(?<=\\.)\\s', '\n')
