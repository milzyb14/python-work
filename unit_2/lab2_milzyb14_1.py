''' Name: Tip Your Server or Bartender Calculator 
    Author: Myles Buchanan 
    Purpose: The purpose of this program is to calculate the tip amount at 15 and 20 percent, 
    as well as the total bill including tip, based on user input of the bill amount.
    Starter code: None
    Date: September 12, 2023
'''

welcome_message = "Welcome to the Tip Your Server or Bartender Calculator!"
print(welcome_message)

bill_total = float(input("Please enter the total bill amount: $"))

welcome_screen = f"{bill_total:.2f}"
print(welcome_screen)