import re

def find_codwars(url):
    return bool(re.match(r''
        '^(https?://)?'   # http(s)://
        '([a-z]+\.)*'     # subdomains
        'codwars\.com'    # codwars.com
        '([/?].*)?$'      # directories or querystrings
        , url))
