def to_camel_case(text):
    return "".join([i if n==0 else i.capitalize() for n,i in enumerate(text.replace("-","_").split("_"))])
