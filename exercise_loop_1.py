
def average():

    var = True

    count = 0

    sum = 0

    while var:

        try:    
    
            temp = input("Enter a number: ")

            number = int(temp)

            list_numbers = []

            list_numbers.append(number)

            for num in list_numbers:

                count += 1

                result = sum + num

                sum = result

        except:

            if temp == "done":                

                var = False

                print(sum,count,sum / count)

            elif temp == "bad data": 
                
                print("Invalid input")        

average()


    