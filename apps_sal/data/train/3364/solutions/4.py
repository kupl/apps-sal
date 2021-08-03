from numpy import linalg as LA


def predict_age(*ages):
    return LA.norm(ages) // 2
