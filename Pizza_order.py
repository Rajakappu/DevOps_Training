print("Thank you for choosing Amazing Pizza Deliveries!")
print("Please select the size of the pizza")
size = input()
print("Do you want to add Pepperoni")
add_pepperoni = input()
print("Do you want to add extra cheese")
extra_cheese = input() 
bill=0
if size=="S":
  bill+=15
elif size=="M":
  bill+=20
else:
  bill+=25

if add_pepperoni=="Y":
  if size=="S":
    bill+=2
  else:
    bill+=3

if extra_cheese=="Y":
  bill+=1

print(f"Your final bill is: ${bill}.")
