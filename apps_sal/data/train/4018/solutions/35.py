def isDigit(st):
    try:
        if int(st.strip()) == 0 or int(st.strip()):
            return True
    except ValueError:
        try:
            if float(st.strip()) or float(st.strip()) == 0.0:
                return True
        except ValueError:
            return False
