import re


def domain_name(url):
    return re.sub('/[a-z]*/?', '', re.sub('\\.[a-z]*', '', re.sub('(https?|www)(://|\\.)', '', url)))
