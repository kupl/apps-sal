def remove_url_anchor(url):
    for letter in url:
        if letter == "#":
            x = url.index(letter)
            return url[0:x]

    return url
    # TODO: complete
