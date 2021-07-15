def namelist(names):
    return " ".join([names[i]["name"] + (" &" if i == len(names)-2 else "" if i==len(names)-1 else ",") for i in range(len(names))])
