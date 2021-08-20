def compare_versions(v1, v2):
    return [int(n) for n in v1.split('.')] >= [int(n) for n in v2.split('.')]
