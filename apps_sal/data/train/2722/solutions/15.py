def remove_url_anchor(s): return __import__('re').sub('(.*)\\#.*', '\\1', s)
