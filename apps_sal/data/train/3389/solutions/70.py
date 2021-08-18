def domain_name(url):
    import re
    result = re.sub('^.*//|www\.', '', url)
    result = re.sub('\..*', '', result)
    return result
