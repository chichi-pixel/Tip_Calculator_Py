#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
#Format the result to 2 decimal places = 33.60
#Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

print("Welcome to the Tip_Calculator!")
bill = float(input("what was the total Bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the Bill!"))


tip_as_percent = tip / 100
total_tip_amount = bill* tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")



