def compare_versions(version1, version2):
    v1 = map(int, version1.split('.'))
    v2 = map(int, version2.split('.'))
    return list(v1) >= list(v2)
