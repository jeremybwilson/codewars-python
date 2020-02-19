# Vasya - clerk
# The new "Avengers" movie has just been released! There are a lot of people 
# at the cinema box office standing in a huge line. Each of them has a single 100, 
# 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially 
# has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change 
# with the bills he has at hand at that moment. Otherwise return NO.

# def foo(n):
#   return sum([int(item) for item in n])

# top voted solution
def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}
    
  for paid in people:
    till[paid] += 1
    change = paid-25.0


  for bill in (50, 25):
    while (bill <= change and till[bill] > 0):
      till[bill] -= 1
      change -= bill

  if change != 0:
    return 'NO'

  return 'YES'


print tickets([25, 25, 50]) # => YES 
print tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
print tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)