# Convert string to camel case

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized.

def to_camel_case(text):

  # text_list = text.replace('-', '_').split('_')
  # answer_list = [text_list[0], ]
  # for word in text_list[1:]:
  #     answer_list.append( word.title() )
  # return ''.join(answer_list)

  # highest voted solution:
  return text[0] + text.title().translate(None, "-_")[1:] if text else text

print to_camel_case('')
print to_camel_case("the-stealth-warrior")
print to_camel_case("The_Stealth_Warrior")
print to_camel_case('The stealTh warrioR')
print to_camel_case('A-B-C')