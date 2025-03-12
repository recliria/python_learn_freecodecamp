
try:
    # Ask to the user, your score
    score = float(input("Enter the score: "))

except:

    print("Error, wrong score")

    score = float(input("Enter the score: "))

# Evaluate user score, if it is between 0 and 10
if score >= 0.9 and score < 10.0:

    print("A")

elif score >= 0.8 and score < 10.0:

    print("B")

elif score >= 0.7 and score < 10.0:

    print("C")

elif score >= 0.6 and score < 10.0:

    print("D")

elif score < 0.6 and score >0:

    print("F")

else:

    print("Bad score")