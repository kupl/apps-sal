from distutils.version import LooseVersion

def compare_versions(version1,version2):
    return LooseVersion(version1) >= LooseVersion(version2)
