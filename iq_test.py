# IQ Test
""" 

Bob is preparing to pass IQ test.
The most frequent task in this test is to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob - to check his answers, he needs a program that among the given numbers
finds one that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)


"""

def iq_test(string):
  #your code here
  numbers = string.split()
  noOdds = 0
  noEvens = 0
  position = 0

  # for i in range from 0 to length of given numbers
  for i in range (0, len(numbers)):
    # if the integer value of index is even
    if(int(numbers[i]) % 2 == 0):
        # increment noEvens count + 1
        noEvens = noEvens + 1
    else:
        # otherwise increment noOdds count + 1
        noOdds = noOdds + 1

  if(noOdds > noEvens):
    # for i in range from 0 to length of given numbers
    for i in range(0, len(numbers)):
      # if the integer value of index is even
      if (int(numbers[i]) % 2 == 0):
        # set the position count to the index value + 1
        position = i+1
  else:
    # for i in range from 0 to length of given numbers
    for i in range(0, len(numbers)):
      # if the integer value of index is even
      if (int(numbers[i]) % 2 != 0):
        # set the position count to the index value + 1
        position = i+1

  return position

print iq_test("2 4 7 8 10") #=> 3 // Third number is odd, while the rest of the numbers are even
print iq_test("1 2 1 1") # => 2 // Second number is even, while the rest of the numbers are odd

def iq_test_v2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

print iq_test_v2("2 4 7 8 10")
print iq_test_v2("1 2 1 1")