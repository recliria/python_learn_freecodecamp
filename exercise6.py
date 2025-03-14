
try:
    # Ask to the user, your score
    score = float(input("Enter the score: "))

except:

    print("Error, wrong score")

    score = float(input("Enter the score: "))

# Evaluate user score, if it is between 0 and 10
def compute_grade(score):

    if score >= 0.9 and score < 10.0:

        grade = "A"

    elif score >= 0.8 and score < 10.0:

        grade = "B"

    elif score >= 0.7 and score < 10.0:

        grade = "C"

    elif score >= 0.6 and score < 10.0:

        grade = "D"

    elif score < 0.6 and score >0:

        grade = "F"

    else:

        grade = "Bad score"

    return grade

grade_result = compute_grade(score)

print(grade_result)