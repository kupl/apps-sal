def remove_url_anchor(url):
    final=""
    for letter in url:
        if letter=="#":
            break
        else:
            final+=letter
    return final
        
    # TODO: complete

