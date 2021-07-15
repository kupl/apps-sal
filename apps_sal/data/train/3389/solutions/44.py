def domain_name(url):
    if url[0:8] == "https://" or url[0:7] == "http://":
        if url[8:12] == "www." or url[7:11] == "www.":
            return url.partition('.')[2].partition('.')[0]
        else:
            return (url.partition('//')[2]).partition('.')[0]
    else:
        if url[0:4] == "www.":
            return url.partition('.')[2].partition('.')[0]
        else:
            return url.partition('.')[0]

