import re

def domain_name(url):
    if 'www.' not in url:
        if '://' in url:
            m = re.search('(?<=//)\S+?(?=\.)', url)
        else:
            m = re.search('\S+?(?=\.)', url)
    else:
        m = re.search('(?<=\.)\S+?(?=\.)', url)

    return m.group(0)
