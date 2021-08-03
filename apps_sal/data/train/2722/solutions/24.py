def remove_url_anchor(url):
    web = []
    for letter in url:
        if letter == '#':
            break
        else:
            web.append(letter)
    return ''.join(web)
