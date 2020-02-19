# Weight for weight
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

# When two numbers have the same "weight", 
# let us class them as if they were strings and not numbers: 
# 100 is before 180 because its "weight" (1) is less than 
# the one of 180 (9) and 180 is before 90 since, 
# having the same "weight" (9) it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# def order_weight(strng):
    # split the numbers up 
    # bar = sorted(strng.split())
    # split up individual numbers and add together again (18 => 9, 100 => 1, 48 => 12)
    # baz = sorted(bar, key=foo)
    # re-order original numbers by sum of numbers in them
    # return the re-ordered string of numbers
#     return " ".join(baz)

# def foo(n):
#   return sum([int(item) for item in n])

# top voted solution
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

print order_weight("103 123 4444 99 2000")
print order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")