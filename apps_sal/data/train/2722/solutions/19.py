def remove_url_anchor(url):
    posicion = url.split('#')
    nuevo = posicion[0:1]
    return ''.join(nuevo)
