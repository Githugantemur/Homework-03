# Sample code

print('Testing 2') # it is an example
print("Testing 2") 

# Basic operators
1+2 # add
5-9 # subtract
5*5 # multiply
5/8 # divide
5**2 # power


# string variable
c = 'hello world 123456789'
cc = "world"
c + cc
c + " " + cc

# concatenate a number to string
c + cc + 5.5 # fail, no string
c + cc + str(5.5) # 'At the row' +  str(rownum)
num = 5.5
c + cc + str(num) # success
c + " " + cc + " " + str(5.5) # space
" ".join([c, cc, str(5.5)]) # join


longtext = "'Ulaanbatar' is the capital city of Mongolia"
longtext = '"Ulaanbatar" is the capital city of Mongolia'
# longtext = ""Ulaanbatar" is the capital city of Mongolia"
print(longtext)



# int, float
b = 35
a = "35"
int(a)+5
float(a)+5

type(float(a))
type(['hello world 123456789', 'world', '5.5'])
type('hi')


# boolean
my_condition0 = True 
my_condition1 = False
age = 30
gender = 'male' # "male"

ifbothtrue = (age > 38) & (gender == 'male') # and
ifonetrue = (age > 28) | (gender == 'female') # or

rownum = 100
print('At the row:', rownum)
print('At the row: ' + str(rownum) + '. Proceeding to the next ...')
print('At the row: ', str(rownum), '. Proceeding to the next ...')

# format string
print('At the row: {}. Proceeding to {}'.format(rownum, rownum + 1))
print(f'At the row: {rownum}. Proceeding to {rownum + 1}')


# input
m = input("Enter a number: ") 
print(f'You entered: {m}. Done!')