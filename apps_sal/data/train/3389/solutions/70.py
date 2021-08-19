def domain_name(url):
    import re
    result = re.sub('^.*//|www\.', '', url)  # del 'http://' and 'www.' (start of url)
    result = re.sub('\..*', '', result)     # del .com, .co.jp, ... (end of url)
    return result
