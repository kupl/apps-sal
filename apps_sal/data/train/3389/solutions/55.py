import re


def domain_name(url):
    url = url.replace('https://', '').replace('http://', '').replace('www.', '')
    print(re.findall('^[^\\.]+', url))
    return re.findall('^[^\\.]+', url)[0]
