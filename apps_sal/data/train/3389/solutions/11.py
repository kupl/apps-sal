def domain_name(url):
    if '//' in url:
        list1 = url.split('//')
    if 'www.' in url:
        list1 = url.split('www.')
    try:
        str1 = list1[1]

        list2 = str1.split('.')
        return(list2[0])
    except:
        list2 = url.split('.')
        return(list2[0])

