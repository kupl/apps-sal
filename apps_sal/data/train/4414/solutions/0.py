def compare_versions(ver1,ver2):
    return [int(i) for i in ver1.split(".")] >= [int(i) for i in ver2.split(".")]

