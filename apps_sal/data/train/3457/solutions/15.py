def final_grade(exam: int, projects: int) -> int:
    """
    Calculates the final grade of a student depending on two parameters:
     - grade for the exam
     - number of completed projects
    """
    return {all([exam > 50, projects >= 2]): 75, all([exam > 75, projects >= 5]): 90, any([exam > 90, projects > 10]): 100}.get(True, 0)
