evil_code_medal = lambda *args: ["None", "Bronze", "Silver", "Gold"][sum(arg > args[0] for arg in args[1:])]
