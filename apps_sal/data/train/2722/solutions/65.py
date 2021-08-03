def remove_url_anchor(url):

    s = ""

    for i in range(len(url)):

        if url[i] == '#':

            break

        else:

            s += url[i]

    return s
