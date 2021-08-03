from re import sub

ignoreList = ["THE", "OF", "IN", "FROM", "BY", "WITH", "AND", "OR", "FOR", "TO", "AT", "A"]


def generate_bc(url, separator):
    # remove leading http(s):// and trailing /
    url = sub("https?://", "", url.strip("/"))

    # skip index files
    url = sub("/index\..+$", "", url)

    # split url for processing
    url = url.split("/")

    # remove file extensions, anchors and parameters
    url[-1] = sub("[\.#\?].*", "", url[-1])

    # first element is always "home"
    menu = ["HOME"]
    # generate breadcrumb items
    for item in url[1:]:
        # replace dashes and set to uppercase
        item = sub("-", " ", item.upper())
        # create acronym if too long
        if len(item) > 30:
            item = "".join([w[0] for w in item.split() if w not in ignoreList])
        menu.append(item)

    # generate paths
    path = ["/"]
    for i in range(len(url) - 1):
        path.append(path[i] + url[i + 1] + "/")

    # generate html code
    html = []
    for i in range(len(url) - 1):
        html.append("<a href=\"" + path[i] + "\">" + menu[i] + "</a>")
    html.append("<span class=\"active\">" + menu[-1] + "</span>")

    return separator.join(html)
