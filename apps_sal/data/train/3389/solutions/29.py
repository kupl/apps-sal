from re import sub


def domain_name(url):
    return sub('^(?:https?:\\/\\/)?(?:www\\.)?([\\w\\-]+)\\.(?:.*?)$', '\\1', url)
