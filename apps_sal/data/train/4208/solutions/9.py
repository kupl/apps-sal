def ipsubnet2list(s):
    try:return[str(x)for x in list(__import__('ipaddress').ip_network(s).hosts())]
    except ValueError: return None
