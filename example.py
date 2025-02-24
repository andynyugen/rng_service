import time

# Function to get number type
def get_type(prompt):
    while True:
        # Prompt user for input
        number_type = input(prompt)
        if number_type in ['int', 'float']:
            return number_type
        # Print error if user did not type valid number type
        else: 
            print("Erorr: Invalid input. Enter int or float")

# Function get number type
def get_number(prompt, number_type):
    while True:
        try:
            # Prompt user for a number
            number = input(prompt)
            if (number_type == 'int'):
                return int(number)
            elif (number_type == 'float'):
                return float(number)
            
        # Print error if user didn't enter int or float
        except ValueError:
            if (number_type == 'int'):
                print("ERROR: Please enter an integer")
            else:
                print("ERROR: Please enter a number")

# Function get decimal place
def get_decimal(prompt, number_type):
    while True:
        try:
            # Prompt user for decimal place
            decimal = int(input(prompt))

            # Reprompt user if they entered invalid decimal place
            if (number_type == 'int' and decimal != 0):
                print("ERROR: Enter 0 for integer")
                continue
            if (number_type == 'float' and decimal < 1):
                print("ERROR: Enter a number greater than 0 for float")
                continue

            # Return if the input was valid
            return decimal
        
        # Print error if user didn't enter number
        except ValueError:
            print("Error: Please enter a valid decimal place")

def main():
    # Welcome user to program
    print("Welcome to Andy's Random-Number Generator")

    # Request user for inputs
    number_type = get_type("Would you like an integer or float? Enter 'int' or 'float': ")
    minimum = get_number("Enter a minimum for your random number: ", number_type)
    maximum = get_number("Enter a maximum for your random number: ", number_type)
    decimal_place = get_decimal("How many decimals? Enter 0 if you wanted an integer: ", number_type)


    # Combine user inputs as a csv string
    data = [number_type, minimum, maximum, decimal_place]
    csv_data = ",".join(map(str, data))

    print("Writing data...")
    # Sleep for 4 seconds
    for i in range(3):
        print(".")
        time.sleep(1)

    with open("data.csv", "w") as file:
        # Write csv string into data file
        file.write(f"{csv_data}")
        
    with open("data.csv", "r") as file:
        # Read data file
        file_string = file.readline().rstrip()

    # Wait to read correct input from file
    while True:
        with open("data.csv", "r") as file:
            file_string = file.readline().rstrip()

        if file_string != csv_data:
            break  # Exit the loop when the file changes

        print(".")
        time.sleep(2)
        
    # Print random generated number to program
    print(f"Random {number_type} number between {minimum} and {maximum}: {file_string}")

if __name__ == "__main__":
    main()