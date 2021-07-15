import re

def generate_bc(url, separator):
    def formater(name):
        if len(name) > 30:
            stoplist = ['the','of','in','from','by','with','and','or','for','to','at','a']
            return ''.join([ch[0].upper() for ch in name.split('-') if ch not in stoplist])
        else:
            return name.replace('-', ' ').upper()
    
    result = []
    
    url = re.sub(r'^https?:\/\/', '', url)      # remove protocol
    url = re.sub(r'\.[^\/]*$', '', url)         # remove extensions
    url = re.sub(r'(?:\#|\?).*$', '', url)      # remove anchors and queries
    url = re.sub(r'index$', '', url)            # remove indexes
    url = url.rstrip('/')                       # remove trailing slash
    
    crumbs = url.split('/')
    
    for i, crumb in enumerate(crumbs):
        if i == 0: result.append('<a href="/">HOME</a>' if len(crumbs) > 1 else '<span class="active">HOME</span>')
        elif i == len(crumbs) - 1: result.append('<span class="active">{}</span>'.format(formater(crumb)))
        else: result.append('<a href="/{}/">{}</a>'.format('/'.join(crumbs[1:1+i]), formater(crumb)))
    
    return separator.join(result)
