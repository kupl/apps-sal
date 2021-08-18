def remove_url_anchor(url):
    accum = []
    for char in url:
        if char != "
        accum.append(char)
        if char == "
        break
    return "".join(accum)
