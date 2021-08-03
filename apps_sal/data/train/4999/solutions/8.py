def capital(capitals):
    result = []

    for i in capitals:
        if "country" in list(i.keys()):
            country_State = "country"
        else:
            country_State = "state"
        result.append("The capital of " + i[country_State] + " is " + i["capital"])
    return result
