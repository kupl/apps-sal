def get_honor_path(honor_score, target_honor_score):
    k1, k2 = divmod(target_honor_score - honor_score, 2)
    return {"2kyus": k2, "1kyus": k1} if honor_score < target_honor_score else {}
