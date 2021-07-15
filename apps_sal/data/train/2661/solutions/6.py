import re
def find_codwars(url):
    m=re.match('(?:https?://)?([\w\.]+)',url)
    domain=m.group(1).split('.')
    return len(domain)>=2 and domain[-2]=='codwars' and domain[-1]=='com'
