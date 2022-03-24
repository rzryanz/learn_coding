biggest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = int(sval)
    except:
        print("Invalid input")
        continue
    if biggest is None or fval > biggest:
        biggest = fval
    if smallest is None or fval < smallest:
        smallest = fval

print("Maximum is", biggest)
print("Minimum is", smallest)
