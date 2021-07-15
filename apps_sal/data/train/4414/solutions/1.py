def compare_versions(version1,version2):
    from distutils.version import LooseVersion, StrictVersion
    return LooseVersion(version1) >= LooseVersion(version2)

