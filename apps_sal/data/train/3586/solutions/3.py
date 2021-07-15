import re
def html(tag,*content,cls=None,**atts):  
    attributes = str(atts).replace('{',"").replace('}',"")
    lst = attributes.split(',')
    lst = [i.replace("'","",2).replace("'",'"').replace(': ',"=",1) for i in lst]
    attributes = "".join(lst)   
    if len(content) > 0:
        txt = ""
        for i in range(len(content)):
            if cls: 
                if attributes:
                    txt += "\n"+f"<{tag} class=\"{str(cls)}\" {attributes}>{content[i]}</{tag}>"
                else:
                    txt += "\n"+f"<{tag} class=\"{str(cls)}\">{content[i]}</{tag}>"
            else:
                if attributes:
                    txt += "\n"+f"<{tag} {attributes}>{content[i]}</{tag}>"     
                else:
                    txt += "\n"+f"<{tag}>{content[i]}</{tag}>"
        return txt[1:]
    else: 
        if cls:
            if attributes:
                return f"<{tag} class=\"{str(cls)}\" {attributes} />"
            else:
                return f"<{tag} class=\"{str(cls)}\" />"
        else:
            if attributes:
                return f"<{tag} {attributes} />"
            else:
                return f"<{tag} />"

