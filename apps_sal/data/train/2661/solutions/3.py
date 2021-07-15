from urllib.parse import urlparse

def find_codwars(url):
    parts = urlparse(url)
    host = parts.netloc or parts.path
    return host == 'codwars.com' or host.endswith('.codwars.com')
