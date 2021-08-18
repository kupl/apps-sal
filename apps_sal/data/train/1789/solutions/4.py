def generate_bc(url, separator):
    a, span = '<a href="%s/">%s</a>', '<span class="active">%s</span>'
    restricted = set("THE OF IN FROM BY WITH AND OR FOR TO AT A".split())

    def bc(menu):
        menu = menu.upper().replace('-', ' ')
        if len(menu) > 30:
            menu = ''.join(w[0] for w in menu.split() if w not in restricted)
        return menu or 'HOME'
    url = ''.join(url.strip('/').rpartition('//')[2].partition('/')[1:]) \
            .rsplit('?', 1)[0].rsplit('
    return separator.join([a % ('/'.join(url[:i]), bc(m)) for i, m in enumerate(url[:-1], 1)] + [span % bc(url[-1])])
