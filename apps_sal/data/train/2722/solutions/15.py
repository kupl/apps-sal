remove_url_anchor = lambda s: __import__('re').sub('(.*)\\#.*', '\\1', s)
