def get_honor_path(honor_score, target_honor_score):
    return {} if honor_score >= target_honor_score else {"2kyus": (target_honor_score - honor_score) % 2, "1kyus": (target_honor_score - honor_score) // 2}
