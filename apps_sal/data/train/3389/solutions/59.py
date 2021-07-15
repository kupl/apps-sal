import re
def domain_name(url):
    return [m for m in re.findall('[(\w+)(?=\-)]+(?=\.)', url) if m != 'www'][0]
