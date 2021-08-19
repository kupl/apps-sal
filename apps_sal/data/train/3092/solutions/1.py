def denumerate(enum_list):
    try:
        (l, d) = (len(enum_list), dict(enum_list))
        ret = ''.join(map(d.get, range(l)))
        assert ret.isalnum() and len(ret) == l
        return ret
    except:
        return False
