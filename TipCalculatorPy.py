#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the Tip_Calculator!")
bill = float(input("what was the total Bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, 15? "))
people = int(input("how many people to split the Bill!"))


tip_as_percent = tip / 100
total_tip_amount = bill* tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")


