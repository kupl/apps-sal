import re


def domain_name(url):
    return re.sub(r'/[a-z]*/?', '', re.sub(r'\.[a-z]*', '', re.sub(r'(https?|www)(://|\.)', '', url)))
