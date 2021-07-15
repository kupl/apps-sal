from distutils.version import LooseVersion


def compare_versions(version1, version2):
    v1 = LooseVersion(version1)
    v2 = LooseVersion(version2)
    return v1 >= v2
