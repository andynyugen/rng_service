import random
import time
import re

def read_request():
    # Open data.txt
    with open("data.csv", "r") as file:
        # Read the first line
        data = file.readline().rstrip()

    # Print error if no data was provided
    if not data:
        print("ERROR: No data provided")
    
    # Else tokenize the csv line string
    else:
        tokens = re.split(",", data)
        return tokens

def write_rand_number(rand_number, number_type, decimal_place):
    # Erase data string from prng-service.txt
    # Write the random number into data.csv
    with open("data.csv", "w") as file:
        # If user requested integer
        if (number_type == "int"):
            file.write(f"{rand_number}") # Write int to file
                
        # Else if, user requested a float
        elif (number_type == "float"):
            rounded_rand = round(rand_number, decimal_place) # Apply decimal places
            file.write(f"{rounded_rand}") # Write float to file


def main():

    print("Retrieving data...")
    # Sleep for 3 seconds
    for i in range(3):
        print(".")
        time.sleep(1)

    # Read request from file "data.csv"
    tokens = read_request()

    # Store the tokens in specific variables
    number_type = tokens[0] # string (int or float)
    minimum = float(tokens[1]) # Minimum bound
    maximum = float(tokens[2]) # Maximum bound
    decimal_place = int(tokens[3]) # Decimal places


    # Generate random number using tokens
            
    # If user requested integer
    if (number_type == "int"):
        # Convert min and max to int user requested integer
        # Generate random number
        rand_number = random.randint(int(minimum), int(maximum))
            
    # Else if, user requested a float
    elif (number_type == "float"):
        # Generate random number
        rand_number = random.uniform(minimum, maximum)

    # Write random number into "data.csv"
    write_rand_number(rand_number, number_type, decimal_place)

if __name__ == "__main__":
    main()