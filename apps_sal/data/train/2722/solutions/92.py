def remove_url_anchor(url):
    ans = '' 
    for i in range(len(url)):
        if url[i]=='#':
            break
        else:
            ans += url[i]
    return ans

