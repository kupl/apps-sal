def domain_name(url):
    print(url)
    start = url[0:3]
    print(start)
    http = "htt"
    www = 'www'
    start2 = url[0:10]
    http2 = 'http://www'
    if start == http and start2 != http2:
        split_list = url.split('//')
        return split_list[1].split('.')[0]
    elif start == www:
        return url.split('.')[1]
    elif start2 == http2:
        return url.split('.')[1]
    else:
        return url.split('.')[0]
