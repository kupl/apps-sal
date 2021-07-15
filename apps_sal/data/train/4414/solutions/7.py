def compare_versions(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    a = max(len(v1), len(v2))
    v1.append('0'*abs(len(v1) - a))
    v2.append('0'*abs(len(v2) - a))
    if v1[-1] == '':
        v1.pop(-1)
    if v2[-1] == '':
        v2.pop(-1)
    k = 0
    for i in v1:
        if int(i) < int(v2[k]):
            return False
        elif int(i) >= int(v2[k]):
            k += 1
    return True
