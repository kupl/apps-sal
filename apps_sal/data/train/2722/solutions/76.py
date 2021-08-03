def remove_url_anchor(url):

    l = ""

    for i in url:
        if i != "#":
            l += i

        else:
            break
    return l
