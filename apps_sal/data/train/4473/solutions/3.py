from itertools import accumulate

XPS = [0, 0, 314]
percent = 125
for i in range(3, 170 + 1):
    XPS.append(XPS[-1] * percent // 100)
    if i % 10 == 0:
        percent -= 1
XPS = list(accumulate(XPS))

def xp_to_target_lvl(current_xp=None, target_lvl=None):
    if not (
        isinstance(current_xp, int)
        and isinstance(target_lvl, int)
        and current_xp >= 0
        and 1 <= target_lvl <= 170
    ):
        return "Input is invalid."
    required = XPS[target_lvl] - current_xp
    return required if required > 0 else f"You have already reached level {target_lvl}."

