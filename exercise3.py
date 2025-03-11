
hours = int(input("Enter the hours: "))

rate = int(input("Enter the rate: "))

if hours > 40:

    pay = hours * (rate * 1.5)

else:

    pay = hours * rate

print(f"The pay is: {pay}")