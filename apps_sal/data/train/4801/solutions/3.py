complaints = ("slow!", "expensive!", "manual!", "down!", "hostage!", "security!")
legacy = {"cobol": 1000, "nonobject": 500, "monolithic": 500, "fax": 100, "modem": 100,
          "thickclient": 50, "tape": 50, "floppy": 50, "oldschoolit": 50}

def roast_legacy(workloads):
    workloads = workloads.lower()
    resolution = sum(workloads.count(complaint) for complaint in complaints)
    score = sum(workloads.count(k) * v for k, v in list(legacy.items()))
    if resolution or score:
        return f"Burn baby burn disco inferno {score} points earned in this roasting and {resolution} complaints resolved!"
    return "These guys are already DevOps and in the Cloud and the business is happy!"

