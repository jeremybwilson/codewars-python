# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 21445 => Output: 54421
# Input: 145263 => Output: 654321
# Input: 1254859723 => Output: 9875543221

def Descending_Order1(num):
    #Bust a move right here
    s = str(num)
    digits = sorted(s, reverse=num>0)
    return int(''.join(digits))

def Descending_Order2(num):
    return int("".join(sorted(str(num), reverse=True)))

num1 = 1445 
num2 = 145263 
num3 = 1254859723

print Descending_Order1(num1)
print Descending_Order1(num2)
print Descending_Order1(num3)
print Descending_Order2(num1)
print Descending_Order2(num2)
print Descending_Order2(num3)
