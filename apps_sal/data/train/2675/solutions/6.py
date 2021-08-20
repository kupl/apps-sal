def bad_apples(apples):
    (good_packages, bad_packages) = ([], [])
    for (i, box) in enumerate(apples):
        if box[0] and box[1]:
            good_packages.append([i, box])
        elif box[0] or box[1]:
            bad_packages.append([i, box[1] if box[1] else box[0]])
    for (a, b) in zip(*[iter(bad_packages)] * 2):
        good_packages.append([a[0], [a[1], b[1]]])
    return [box for (_, box) in sorted(good_packages)]
