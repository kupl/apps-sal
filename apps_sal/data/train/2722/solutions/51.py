def remove_url_anchor(url):
    c=""
    for ch in url:
        if ch== "#":
            break
        c+=ch
    return c
