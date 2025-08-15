from art import logo
print(logo)

continue_bidding = True
auction = {}

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    highest_bid_name = ""

    for key in bidding_dictionary:
        if bidding_dictionary[key] > highest_bid:
            highest_bid = bidding_dictionary[key]
            highest_bid_name = key
    print(f"The winner is {highest_bid_name} with a bid of {highest_bid}")

while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid?: "))
    auction[name] = bid
    other_bidders = input("Is there any other bidders? Type \"Yes\" or \"No\".\n").lower()
    if other_bidders == "no":
        continue_bidding = False
        find_highest_bidder(auction)
    print("\n" * 10)
