def remove_url_anchor(url):
    # TODO: complete
    new_url = ""
    for char in url:
        if char == "#":
            break
        new_url = new_url + char

    return new_url
