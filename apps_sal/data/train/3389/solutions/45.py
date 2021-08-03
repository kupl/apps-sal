import re


def domain_name(url):
    url = re.sub(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/|www\.)', '', url)
    return re.sub(r'\..+', '', url)
