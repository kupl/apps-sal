def remove_url_anchor(url):
    ans = ''
    for index in range(0, len(url)):
        if url[index] != '#':
            ans += url[index]
        else:
            break
    return ans
