dict = {10: "A", 9: "A", 8: "B", 7: "C", 6: "D"}


def get_grade(s1, s2, s3):
    mean = int((s1 + s2 + s3) / 30)
    if mean in dict:
        return dict[mean]
    return "F"
