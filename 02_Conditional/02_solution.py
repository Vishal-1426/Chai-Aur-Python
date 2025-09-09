#  Q:2 Movie Ticket Pricing
# Problem: Movie tickets are priced based on age:$12 adults(18 and over),$8 for childern,Everyone gets a $2 discount on Wednesday.

age = 22
day = "Wednesday"

price = 12 if age >= 18 else 8
if day == "Wednesday":
  price = price - 2

  print("Ticket price for you is $", price)