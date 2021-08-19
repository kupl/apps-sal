import re


def base_name(fullname):
    return re.sub('[.].*$', '', fullname)


ignore_words = ['the', 'of', 'in', 'from', 'by', 'with', 'and', 'or', 'for', 'to', 'at', 'a']


def short_name(name):
    if len(name) <= 30:
        return re.sub('[-]', ' ', name)
    else:
        return ''.join([a[0] for a in name.split('-') if a not in ignore_words])


def generate_bc(url, separator):
    url_striped = re.sub('[#?].*', '', url)
    url_striped = re.sub('(http|https)://', '', url_striped)
    url_striped = re.sub('/$', '', url_striped)
    url_splited = url_striped.split('/')
    if base_name(url_splited[-1]) == 'index':
        del url_splited[-1]
    if len(url_splited) <= 1:
        return '<span class="active">HOME</span>'
    path = '/'
    res = list()
    res.append('<a href="/">HOME</a>')
    for e in url_splited[1:-1]:
        path += e + '/'
        res.append('<a href="%s">%s</a>' % (path, short_name(e).upper()))
    res.append('<span class="active">%s</span>' % short_name(base_name(url_splited[-1])).upper())
    return separator.join(res)
