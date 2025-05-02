# Write a program that examines three variables—x, y, and z—and prints the largest odd number among them. 
# If none of them are odd, it should print a message to that effect.
try:
var_x = int(input('Enter value of x: '))
var_y = int(input('Enter value of y: '))
var_z= int(input('Enter value of z: '))
except ValueError:
    print("Please enter valid integers")
    exit()
odd_num = []
if var_x % 2 != 0: 
    odd_num.append(var_x)
if var_y % 2 != 0: 
    odd_num.append(var_y)
if var_z % 2 != 0: 
    odd_num.append(var_z)
if len(odd_num)==0:
    print ('You entered no odd numbers') 
else: 
    print(f'The largest odd number is {max(odd_num)}')     

