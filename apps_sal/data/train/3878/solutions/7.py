def kangaroo(kanga1, rate1, kanga2, rate2):
    if kanga1 == kanga2:
        return True
    elif kanga1 < kanga2:
        velocidad_acercamiento = rate1 - rate2
        if velocidad_acercamiento <= 0:
            return False
        else:
            if (kanga2-kanga1) % velocidad_acercamiento == 0:
                return True
            else:
                return False
    else:
        velocidad_acercamiento = rate2 - rate1
        if velocidad_acercamiento <= 0:
            return False
        else:
            if (kanga1-kanga2) % velocidad_acercamiento == 0:
                return True
            else:
                return False

