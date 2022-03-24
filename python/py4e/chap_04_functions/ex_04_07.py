def compute_grade(numeric_grade):
    if 0 <= numeric_grade <= 1:
        if numeric_grade >= 0.9:
            print("A")
        elif numeric_grade >= 0.8:
            print("B")
        elif numeric_grade >= 0.7:
            print("C")
        elif numeric_grade >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Bad score")


score = input("Enter score: ")
try:
    numeric_grade = float(score)
    letter_grade = compute_grade(numeric_grade)
except:
    print("Bad score")
    quit()
