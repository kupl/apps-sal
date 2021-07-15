from re import sub
remove_url_anchor = lambda url: sub('#.*', '', url)
