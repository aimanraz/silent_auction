from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

# function to insert the bidder
def add_user (bidder_name,bid_amount):
  new_data = {
  "name":bidder_name,
  "amount":int(bid_amount)
  }
  data.append(new_data)

data = [] # stored all bidder
num = 0

print(logo)
print("Welcome to the secret auction program.")
should_continue = True 

while should_continue: # program loop
  # user input
  names = input("What is your name?: ")
  bid = input("What's your bid?: ")
  clear()
  add_user(bidder_name=names,bid_amount=bid)
  # stored highest user bidder
  for i in range(len(data)):
    if data[i]['amount'] > num:
      winner = data[i]['name']
      num = data[i]['amount']
  # ask to continue adding bidder or no
  cont = input("\nAre they other bidders? Type 'yes or 'no' ").lower()
  clear()
  if cont == 'no':
    should_continue = False
    # print the winner
    print(f"The winner is {winner}!, with ${num} bid amount.")
  else:
    clear()



