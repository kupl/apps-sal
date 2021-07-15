def next_version(version):
    if version.count('.')==0: return str(int(version)+1)
    elif int(version[-1])<9: return version[0:-1] + str(int(version[-1])+1)
    else: return next_version(version[0:-2]) + '.0'
