# Write a program that asks user for an integer and prints two integers, root and pwr
# such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

found = False
for pwr in range(1, 6):  # pwr from 1 to 5
    # Trying positive roots first
    root = 0
    while root <= abs(number):
        if root ** pwr == number:
            print(f"root = {root}, pwr = {pwr}")
            found = True
            break
        root += 1
    if found:
        break
    
    # Trying negative roots if number is negative and pwr is odd
    if number < 0 and pwr % 2 == 1:
        root = -1
        while root >= -abs(number):
            if root ** pwr == number:
                print(f"root = {root}, pwr = {pwr}")
                found = True
                break
            root -= 1
        if found:
            break

if not found:
    print("No such pair of integers exists.")