#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percent = float(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people are splitting the bill? "))

bill = total * (1 + percent / 100) / people
final_bill = round(bill, 2)
final_bill = "{:.2f}".format(bill)
message = f"Each person should pay: ${final_bill}"
print(message)