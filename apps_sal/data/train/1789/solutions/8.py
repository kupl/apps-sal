def generate_bc(url, separator):
    print(url)
    print(separator)
    url = str(url.replace("https://", ""))
    url = str(url.replace("http://", ""))

    try:
        questionIndex = url.index("?")
    except ValueError:
        questionIndex = -1

    try:
        hashIndex = url.index("
    except ValueError:
        hashIndex=-1

    if questionIndex != -1:
        url=str(url[:questionIndex])

    if hashIndex != -1:
        url=str(url[:hashIndex])

    names=list(filter(None, url.split('/')))
    html=""

    commonExtensions=[".html", ".htm", ".php", ".asp"]
    ignoreWords=[
        "the",
        "of",
        "in",
        "from",
        "by",
        "with",
        "and",
        "or",
        "for",
        "to",
        "at",
        "a"
    ]
    pastLinks=[]

    for index, name in enumerate(names):
        isFirstIndex=index == 0
        isLastIndex=index == len(names) - 1

        if not isLastIndex and "index" in names[index + 1]:
            isLastIndex=True

        if isLastIndex:
            for commonExtension in commonExtensions:
                name=name.replace(commonExtension, "")

        tagValue=""
        if isFirstIndex:
            tagValue="HOME"
        elif len(name) > 30:
            tagValue=''.join(
                str.upper(a[0:1]) for a in name.split('-') if a not in ignoreWords)
        else:
            if '-' in name:
                tagValue=name.upper().replace('-', ' ')
            else:
                tagValue=name.upper()

        html += "<{element}".format(element='span' if isLastIndex else 'a')
        if isLastIndex:
            html += ' class="active"'
        else:
            currentLink=name.strip().lower()
            hrefValue=''
            if isFirstIndex:
                hrefValue='/'
            elif len(pastLinks) > 0:
                pastLinks.append(currentLink)
                hrefValue='/{link}/'.format(link="/".join(pastLinks))
            else:
                pastLinks.append(currentLink)
                hrefValue="/{link}/".format(link=currentLink)
            html += ' href="{hrefValue}"'.format(hrefValue=hrefValue)

        html += '>'
        html += tagValue
        html += '</{attribute}>'.format(
            attribute='span' if isLastIndex else 'a')
        if not isLastIndex:
            html += separator
        if isLastIndex:
            break

    return html
