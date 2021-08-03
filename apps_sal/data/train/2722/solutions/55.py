def remove_url_anchor(url):
    l1 = list()
    for i in range(len(url)):
        if(url[i] != '#'):
            l1.append(url[i])
        else:
            break
    return ''.join(l1)
