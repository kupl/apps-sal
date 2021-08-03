import unittest


def final_grade(exam, projects):
    print((exam, projects))
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


class TestFinalGrade(unittest.TestCase):
    def test_final_grade_on_100_with_exam_score_that_is_more_than_90(self):
        exam, projects = 100, 12
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 100)

    def test_final_grade_on_100_with_projects_that_is_more_than_10(self):
        exam, projects = 80, 10
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 100)

    def test_final_grade_on_90_with_exam_score_that_is_more_than_75(self):
        exam, projects = 75, 3
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 90)

    def test_final_grade_on_90_with_projects_that_is_more_than_5(self):
        exam, projects = 70, 5
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 90)

    def test_final_grade_on_75_with_exam_score_that_is_more_than_50(self):
        exam, projects = 50, 3
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 75)

    def test_final_grade_on_75_with_projects_that_is_more_than_2(self):
        exam, projects = 40, 3
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 75)

    def test_final_grade_on_0_with_projects_and_exam_score_that_is_less_than_final_grade_on_75(self):
        exam, projects = 30, 1
        actual = final_grade(exam, projects)
        self.assertEqual(actual, 0)
