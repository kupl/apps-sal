def get_honor_path(honor, target):
    return dict(list(zip(["1kyus", "2kyus"], divmod(target - honor, 2)))) if target > honor else {}

