from urllib.parse import urlparse


def domain_name(url):
    parsed = urlparse(url)
    dom = parsed.netloc
    path = parsed.path
    if dom:
        dom_spl = dom.split('.')
        if dom_spl[0] == 'www':
            return dom_spl[1]
        return dom_spl[0]

    elif path:
        path_spl = path.split('.')
        if path_spl[0] == 'www':
            return path_spl[1]
        return path_spl[0]
