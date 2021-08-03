def remove_url_anchor(url):
    final_url = ''
    for i in url:
        if i == '#':
            return final_url
        final_url += i
    return final_url
