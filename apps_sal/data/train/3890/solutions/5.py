def get_honor_path(honorScore, targetHonorScore):
    return {'1kyus': (targetHonorScore - honorScore) // 2, '2kyus': (targetHonorScore - honorScore) % 2} if targetHonorScore > honorScore else {}
