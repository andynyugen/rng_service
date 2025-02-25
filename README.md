# rng_service
Communication Pipe: "data.csv" (text file)

# Requesting Data
To request data user must supply 4 inputs as a csv (comma separated value) line string and write it into "data.csv".
  1. Number type - "int" or "float"
  2. Minimum bound for the number
  3. Maximum bound for the number
  4. Number of Decimal Places for the number
* Ensure the 4 inputs are valid. Make sure to check for error handling.

csv line: [number type],[minimum],[maximum],[decimal places]

example: int,-60,192,0

example2: float, -30.23, -40.69, 4

example code in python

![image](https://github.com/user-attachments/assets/5094d9d0-3d0b-4760-bc33-68ef4d13a572)


# Receive Data
To receive data, program must be able to read the first line of the csv file.
  1. Random number within range specified by user's inputs as a csv line
     
example: -111

example2: -36.1234

example code in python

![image](https://github.com/user-attachments/assets/1ae45f98-3df1-4ac5-aeea-6e27d78318ff)
* Ensure you read an individual number and not the csv line written in the beginning


# UML Sequence Diagram

![UML Sequence Diagram](https://github.com/user-attachments/assets/b3d3c746-7a7d-4449-810a-a5007b3dda56)
