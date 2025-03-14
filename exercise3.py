
try:

    hours = int(input("Enter the hours: "))

    rate = int(input("Enter the rate: "))

except:

    print("Error, please enter numeric input")

    hours = int(input("Enter the hours: "))

    rate = int(input("Enter the rate: "))

def compute_pay(hours,rate):   
    

    if hours > 40:

        pay = hours * (rate * 1.5)

    else:

        pay = hours * rate

    print(f"The pay is: {pay}")  


compute_pay(hours,rate)