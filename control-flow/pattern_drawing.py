# pattern_drawing.py

# Ask user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Row counter using while loop
row = 0
while row < size:
    # Print each column in the row using for loop
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after row
    row += 1
