is_valid=lambda idn: bool(__import__("re").match("^[a-zA-Z_$][\w$]*$",idn))

