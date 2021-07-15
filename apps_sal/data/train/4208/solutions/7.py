def ipsubnet2list(subnet):
    import ipaddress
    ls=[]
    try:
        for i in ipaddress.IPv4Network(subnet):
            ls.append(str(i))
    except :
        return None
    return ls[1:-1] if len(ls)>2 else ls
