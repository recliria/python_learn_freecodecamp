# Print out the number smallest and biggest of a list
def min_max_list_numbers():

    list_numbers = []

    while len(list_numbers) < 5:

        try:
    
            number = int(input("Enter a number: "))

            list_numbers.append(number)            

        except:

            print("Error, you has not written a number")
    
    num1 = list_numbers[0]

    for num in list_numbers:

        if num < num1:

            num1 = num                               

        else:

            continue

    print("The number smallest is:", num1)

    num1 = list_numbers[0]

    for num in list_numbers:

        if num > num1:

            num1 = num                    

        else:

            continue
    
    print("The number biggest is:", num1)

min_max_list_numbers()

