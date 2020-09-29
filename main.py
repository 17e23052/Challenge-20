#This program converts a number entered into its binary and hexadecimal equivalents.
from time import sleep
print("Enter a number between 0 and 255:")
number = int(input())
if number >= 256 or number < 0:
  print("Please enter a number between 0 or 255")
  sleep(999)
binary = bin(number)
print(f"The binary of this number is {binary}")
hexa = hex(number)
print(f"The hexadecimal of this number is {hexa}")
#Please ignore the 0b on the binary answer and the 0x on the hexadecimal answer.