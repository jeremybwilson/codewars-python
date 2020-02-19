# Sum of odd numbers
# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3

print row_sum_odd_numbers(1)
print row_sum_odd_numbers(2)
print row_sum_odd_numbers(3)
print row_sum_odd_numbers(4)
print row_sum_odd_numbers(5)
print row_sum_odd_numbers(6)