def remove_url_anchor(url):
    new_url_lst = []
    new_url = ''
    for i in url:
        if i != '#':
            new_url_lst.append(i)
        else:
            break
    return ''.join(new_url_lst)
