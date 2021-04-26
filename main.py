from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bid_dict = {}
bid_ongoing=True
while bid_ongoing==True:
  name = input("Plese enter your name:")
  bid = int(input("Please enter your bid: $"))
   
  bid_dict[name]=bid
  clear()
  qn = input("Are there anyone else bidding?'yes' or 'no'")
  if qn.lower() =="no":
    bid_ongoing=False

print(bid_dict)
heighest_bid = 0
for bids in bid_dict:
  if bid_dict[bids]>heighest_bid:
    heighest_bid=bid_dict[bids]
    winner = bids

print(f"The winner is {winner} with the bid of {heighest_bid}")

  