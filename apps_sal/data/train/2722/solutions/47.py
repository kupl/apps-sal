def remove_url_anchor(url):
    url_list = list(url) 
    if '#' in url_list: 
        index = url_list.index("#")
        url_list = url_list[:index]
    
    return ("".join(url_list))
        
    # TODO: complete

