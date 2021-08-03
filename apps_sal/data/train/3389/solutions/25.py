import re


def domain_name(url):
    return re.findall('(?:http[s]?://)?(?:www\.)?([0-9a-zA-Z\-]+)\..*', url)[0]
