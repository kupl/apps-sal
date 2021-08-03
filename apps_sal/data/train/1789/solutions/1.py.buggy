common_extensions = ["html", "htm", "php", "asp", "jsp"]
acronym_ignore = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
protocols = ["http://", "https://"]
home_tpl = "<a href=\"/\">HOME</a>"
span_tpl = "<span class=\"active\">%s</span>"
link_tpl = "<a href=\"%s\">%s</a>"


def generate_bc(url, separator):
    """
    Turn an url into an html breadcrumb
    """
    print url
    url = no_protocol(url)
    bread = home_tpl
    crumbs = url.split("/")[1:]
    crumbs = [c for c in crumbs if not(is_index(c)) and len(c) > 0]
    previous = "/"
    print crumbs
    if len(crumbs) == 0:
        return "<span class=\"active\">HOME</span>"
    for crumb in crumbs[:-1]:
        previous, html = knead(crumb, previous)
        bread += separator + html
    bread += separator + brown(crumbs[-1])
    return bread


def knead(crumb, previous):
    """
    Turn a crumb into breadcrumb element
    :param crumb Url part to turn into breadcrumb part
    :param previous url part if any
    :return Tuple containing url and html Breadcrumb element (url, html)
    """
    assert type(crumb) is str
    assert type(previous) is str
    crumb = no_extension(no_params(crumb))
    url = previous + crumb + "/" 
    name = to_acronym(crumb, "", 30)
    name = name.upper()
    return url, link_tpl % (url, name)


def brown(crumb):
    """
    Brown the last crumb into an active span
    :param url_part URL part to check
    :return HTML active span for the crumb
    """
    assert type(crumb) is str
    name = to_acronym(no_extension(no_anchor(no_params(crumb))), " ", 30)
    return span_tpl % (name.upper())


def to_acronym(url_part, joiner, max):
    """
    Turn the given string into an acronym if the size > :max
    :param url_part URL part to check
    :param joiner char to place between word
    :max max number of letter allowed before turning the string into an acronym
    :return Name or acronym if size is too big
    """
    assert type(url_part) is str
    assert type(joiner) is str
    assert type(max) is int
    if len(url_part) >= max:
        url_part="".join([word[0] for word in url_part.split("-") if word not in acronym_ignore])
    return url_part.replace("-", " ")


def is_index(url_part):
    """
    Check if url part is index
    :param url_part URL part to check
    :return True if the name of the element is index.something
    """
    assert type(url_part) is str
    return "index" in url_part


def no_extension(url_part):
    """
    Remove common extension from the end of the url part
    :param url_part URL part to treat
    :return url part as a string without any known extension
    """
    assert type(url_part) is str
    splitted = url_part.split(".")
    if splitted[-1] in common_extensions:
        splitted = splitted[:-1]
    return '.'.join(splitted)
    
    
def no_params(url_part):
    """
    Remove uri params
    :param url_part URL part to treat
    :return url part as a string without uri params
    """
    assert type(url_part) is str
    return url_part.split("?")[0]
    

def no_protocol(url):
    """
    Remove protocol from url string
    :param url URL to strip
    :return URL string without protocol
    """
    assert type(url) is str
    for p in protocols:
        if url.startswith(p):
            url = url[len(p):]
    return url
    

def no_anchor(url_part):
    """
    Remove anchor from url
    :param url_part URL part to treat
    :return url part as a string without anchor
    """
    assert type(url_part) is str
    return url_part.split("#")[0]
