def obfuscate(email):
    obemail = ""
    for l in email:
      if l == "@":
        obemail += " [at] "
      elif l == ".":
        obemail += " [dot] "
      else:
        obemail += l
    return obemail
