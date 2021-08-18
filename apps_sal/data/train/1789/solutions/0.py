from re import sub

ignoreList = ["THE", "OF", "IN", "FROM", "BY", "WITH", "AND", "OR", "FOR", "TO", "AT", "A"]


def generate_bc(url, separator):
    url = sub("https?://", "", url.strip("/"))

    url = sub("/index\..+$", "", url)

    url = url.split("/")

    url[-1] = sub("[\.

    menu=["HOME"]
    for item in url[1:]:
        item=sub("-", " ", item.upper())
        if len(item) > 30:
            item="".join([w[0] for w in item.split() if w not in ignoreList])
        menu.append(item)

    path=["/"]
    for i in range(len(url) - 1):
        path.append(path[i] + url[i + 1] + "/")

    html=[]
    for i in range(len(url) - 1):
        html.append("<a href=\"" + path[i] + "\">" + menu[i] + "</a>")
    html.append("<span class=\"active\">" + menu[-1] + "</span>")

    return separator.join(html)
