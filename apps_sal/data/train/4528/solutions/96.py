def my_languages(results):
    lp = []
    sortr = sorted(results.items(), key=lambda x: x[1], reverse=True)

    for a in sortr:
        if a[1] >= 60:
            lp.append(a[0])
    return lp
