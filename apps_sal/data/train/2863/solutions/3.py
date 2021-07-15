def alan_annoying_kid(stg):
    s1 = stg.replace("Today I ", "")[:-1]
    s3 = s1.replace("didn't ", "").split()[0]
    s2, s3, s4 = ("did", s3, "it") if "n't" in s1 else ("didn't", s3[:-2], "at all")
    return f"I don't think you {s1} today, I think you {s2} {s3} {s4}!"
