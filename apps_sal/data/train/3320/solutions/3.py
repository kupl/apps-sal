def oracle(arr):
    return "\n".join("----{}----".format("x- o"[item.count("h")])
                     for item in sorted(arr, key=lambda x: "six five four three two one".index(x[0])))
