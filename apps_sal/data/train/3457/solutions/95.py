def final_grade(ex, prj):
    return 100 if ex>90 or prj>10 else 90 if ex>75 and prj>=5 else 75 if ex>50 and prj>=2 else 0
