def get_ages(sum_, difference):
    ret = ((sum_ + difference) / 2, (sum_ - difference) / 2)
    if difference < 0 or (ret[1] < 0 or ret[0] < 0):
        return None
    else:
        return ret
