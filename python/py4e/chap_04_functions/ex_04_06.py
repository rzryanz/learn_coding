def compute_pay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

p = compute_pay(fh, fr)

print("Pay", p)
