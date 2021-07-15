def get_honor_path(score, target):
    return {'1kyus':(target-score)//2, '2kyus':(target-score)%2} if target > score else {}
