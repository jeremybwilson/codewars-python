# Regex Password validation
""" 
AYou need to write regex that will validate a password 
to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.


(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z\d]{6,15}$

^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
"""

from re import compile, VERBOSE

# create a regular expression object that we can use run operations on
pw = ''
# regex1 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
regex2 = compile((?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])([A-Za-z\d]{6,15})$, VERBOSE)

def validate_password(pw):
  match = re.match(regex2, pw)
  if match:
    return True
  else:
    return False

validate_password('abcD123b')