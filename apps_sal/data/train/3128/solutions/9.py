import re;is_mac_48_address=lambda s,a='[0-9][A-F]|[0-9]{2}|[A-F]{2}|[A-F][0-9]':len(re.findall(r'-|{}'.format(a),s))==11
