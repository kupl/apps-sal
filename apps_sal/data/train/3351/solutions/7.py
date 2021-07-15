evil_code_medal=lambda t,*m:next((s for s,n in zip(("Gold","Silver","Bronze"),m)if t<n),"None")
