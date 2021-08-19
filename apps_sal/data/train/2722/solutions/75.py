def remove_url_anchor(url):
    newString = ''
    for i in url:
        if i != '#':
            newString = newString + i
        if i == '#':
            break
    return newString
