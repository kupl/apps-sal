import re


def domain_name(url):
    return re.search('(?:https?://)?(?:w{3}\\.)?(.*?)\\..*', url).group(1)
