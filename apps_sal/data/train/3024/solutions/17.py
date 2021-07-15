def friend(x):
    shouldBe = list()
    for f in x:
        if len(f) == 4:
            shouldBe.append(f)
    return shouldBe
