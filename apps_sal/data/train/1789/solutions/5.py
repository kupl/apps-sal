IGNORE = "THE OF IN FROM BY WITH AND OR FOR TO AT A".split()

def generate_bc(url, separator):
    if url.startswith("http"):
        url = url.split("//")[1]
    crumbs = url.split("/")
    links  = crumbs[1:]
    crumbs[0] = 'HOME'
    for i, crumb in enumerate(crumbs):
        crumb = crumb.split(".")[0].split("?")[0].split("#")[0].replace("-", " ").upper()
        if len(crumb) > 30:
            crumb = [c for c in crumb.split() if c not in IGNORE]
            crumb = ''.join(map(lambda c: c[0], crumb))            
        crumbs[i] = crumb
    if crumbs[-1] in ('', 'INDEX'):
        crumbs.pop()
    output = []
    for i, crumb in enumerate(crumbs[:-1]):
        element = '<a href="/%s/">%s</a>' % ("/".join(links[:i]), crumb)
        output += [element.replace("//", "/")]
    output += ['<span class="active">%s</span>' % crumbs[-1]]
    return separator.join(output)
