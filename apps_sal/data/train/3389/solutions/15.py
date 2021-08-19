import re


def domain_name(url):
    if url.find('://') == -1:
        url += '://' + url
    return re.findall('.*\\://(?:www.)?([^\\/]+)', url)[0].partition('.')[0]
