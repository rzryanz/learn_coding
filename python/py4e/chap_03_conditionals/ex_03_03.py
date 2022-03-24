score = input("Enter Score: ")

try:
    fs = float(score)
except:
    print("Please enter a numeric number.")
    quit()

if fs < 0:
    print("Please enter a score between 0.0 and 1.0")
    quit()
elif fs > 1:
    print("Please enter a score between 0.0 and 1.0")
    quit()
elif fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
else:
    print("F")
