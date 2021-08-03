# Defines the function
def check_alive(health):
    # Checks if health parameter is less than or equal to 0.
    if health <= 0:
        # if health is less than or equal to 0 you would be dead. So returns false
        return False
    else:
        # if health is greater than zero you would not be dead. So returns true.
        return True
