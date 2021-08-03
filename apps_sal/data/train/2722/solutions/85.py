def remove_url_anchor(url):
    ans = ''
    for char in url:
        if char is '#':
            break
        ans += char
    return ans
