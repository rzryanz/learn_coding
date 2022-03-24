string_hours = input("Enter hours: ")
string_rate = input("Enter rate: ")
float_hours = float(string_hours)
float_rate = float(string_rate)

if float_hours > 40:
    pay = 40 * float_rate + (float_hours - 40) * float_rate * 1.5
else:
    pay = float_hours * float_rate

print(pay)
