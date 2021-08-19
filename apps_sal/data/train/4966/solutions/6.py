def fight(robot_1, robot_2, tactics):
    # your code
    "who has the higher speed"
    if robot_1["speed"] >= robot_2["speed"]:
        robotfast = robot_1
        robotslow = robot_2
    else:
        robotfast = robot_2
        robotslow = robot_1

    def roundfight(robotfast, robotslow, tactics):

        if len(robotfast["tactics"]) > 0:
            tactic = robotfast["tactics"][0]
            damage = tactics[tactic]
            robotfast["tactics"].pop(0)
            robotslow["health"] -= damage
            "attack 1" "robot fast"
            "how much damage by attack"
            "robot slow loses health"

        "is robotslow alive"
        if robotslow["health"] <= 0:
            return robotfast["name"] + " has won the fight."

        if len(robotslow["tactics"]) > 0:
            tactic = robotslow["tactics"][0]
            damage = tactics[tactic]
            robotslow["tactics"].pop(0)
            robotfast["health"] -= damage

        if robotfast["health"] <= 0:
            return robotslow["name"] + " has won the fight."

        "special case: out of tactics"
        if len(robotfast["tactics"]) == 0 & len(robotslow["tactics"]) == 0:
            if robotfast["health"] == robotslow["health"]:
                return "The fight was a draw."
            elif robotfast["health"] > robotslow["health"]:
                return robotfast["name"] + " has won the fight."
            else:
                return robotslow["name"] + " has won the fight."

        else:
            return roundfight(robotfast, robotslow, tactics)

    return roundfight(robotfast, robotslow, tactics)
