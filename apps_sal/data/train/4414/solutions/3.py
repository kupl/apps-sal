from distutils.version import LooseVersion, StrictVersion
def compare_versions(v1,v2):
    return LooseVersion(v1) >= LooseVersion(v2)
