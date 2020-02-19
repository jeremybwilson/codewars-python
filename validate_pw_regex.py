# Regex Password validation
""" 
AYou need to write regex that will validate a password 
to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.

^(?=.*(\d|\W)).{6,15}$

^                         # match the beginning of the input
(?=                       # start positive look ahead
  .*                      #   match any character except line breaks and repeat it zero or more times
  (                       #   start capture group 1
    \d                    #     match a digit: [0-9]
    |                     #     OR
    \W                    #     match a non-word character: [^\w]
  )                       #   end capture group 1
)                         # end positive look ahead
.{5,20}                   # match any character except line breaks and repeat it between 5 and 20 times
$                         # match the end of the input


(?!^[0-9 ]*$)(?!^[a-zA-Z ]*$)^([a-zA-Z0-9 ]{6,15})$

using lookaheads in regex

 ^      start of input
 (?=.*?[A-Z]) lookahead to make sure there is at least one upper case letter
 (?=.*?[a-z]) lookahead to make sure there is at least one lower case letter
 (?=.*?[0-9]) lookahead to make sure tthere is at least one number
 [A-Za-z0-9]{6,} Make sure there is at least 6 characters of [A-Za-z0-9]
 $      end of input

"""

import re
# create a regular expression object that we can use run operations on
pw = ''
regex = re.compile(r'(?!^[0-9 ]*$)(?!^[a-zA-Z ]*$)^([a-zA-Z0-9 ]{6,15})$')

def validate_password(pw):
  # method 1
  match = re.match(regex, pw)
  if match:
    return True
  else:
    return False

print validate_password("abC1")       # == False
print validate_password("12345Abc")   # == True
print validate_password("a234B56yz")  # == True
print validate_password('fjd3IR9')    # == True
print validate_password('ghdfj32')    # == True
print validate_password('DSJKHD23')   # == True
print validate_password('dsF43')      # == False
