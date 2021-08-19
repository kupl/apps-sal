def remove_url_anchor(url):
    line = []
    for x in url:
        if x != '#':
            line.append(x)
        else:
            break
    return ''.join(line)
