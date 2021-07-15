def domain_name(url):
    import re
    return re.search('(https://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')
