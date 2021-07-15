from re import sub

def domain_name(url):
    return sub(r'^(?:https?:\/\/)?(?:www\.)?([\w\-]+)\.(?:.*?)$', r'\1', url)
