# Regex PIN validation for 4 or 6 digit PIN codes
""" 
ATM machines allow 4 or 6 digit PIN codes 
and PIN codes cannot contain anything 
but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""

def validate_pin(pin):
  # method 1
  return len(pin) in (4, 6) and pin.isdigit()
  # method 2
  # return bool(re.match(r'^(\d{4}|\d{6})$',pin))

print validate_pin("1234")  # == True
print validate_pin("12345")  # == False
print validate_pin("a234")  # == False