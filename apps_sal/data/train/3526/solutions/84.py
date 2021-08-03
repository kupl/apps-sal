def any_arrows(arrows):
    # your code here
    for item in arrows:

        try:
            a = item["damaged"]
            if not a:
                return True
        except:
            return True
    return False
