print ("NFG Coordinate checker - Made by El_Capitano")
print ("")
print ("Special thanks to nonDucor from stackoverflow!")
print ("")
print('Your input should be of the form: 1923 1682')
print ("")
print ("Click below to type!")
guess = input()
try:
    x, y = [int(val) for val in guess.split()]
except:   # This is a very crude check.
    print('Wrong input format')
    raise

# Limits of the rectangle
x_low = 1120
x_high = 1182
y_low = 1360
y_high = 1398

if (x_low <= x <= x_high) and (y_low <= y <= y_high):
        print ("Coordinates are in the B3 NFG area")
else:
        print ("Coordinates are NOT in the B3 NFG area")
try:
    x, y = [int(val) for val in guess.split()]
except:   # This is a very crude check.
    print('Wrong input format')
    raise

# Limits of the rectangle
x_low = 776
x_high = 806
y_low = 1120
y_high = 1142

if (x_low <= x <= x_high) and (y_low <= y <= y_high):
        print ("Coordinates are in the NFG area near A1 shrine")
else:
        print ("Coordinates are NOT in the NFG area near A1 shrine")
try:
    x, y = [int(val) for val in guess.split()]
except:   # This is a very crude check.
    print('Wrong input format')
    raise

# Limits of the rectangle
x_low = 1392
x_high = 1422
y_low = 1656
y_high = 1686

if (x_low <= x <= x_high) and (y_low <= y <= y_high):
        print ("Coordinates are in the C5 NFG area")
else:
        print ("Coordinates are NOT in the C5 NFG area")
try:
    x, y = [int(val) for val in guess.split()]
except:   # This is a very crude check.
    print('Wrong input format')
    raise

# Limits of the rectangle
x_low = 1000
x_high = 1022
y_low = 1808
y_high = 1830

if (x_low <= x <= x_high) and (y_low <= y <= y_high):
        print ("Coordinates are in the D4 zone NFG area")
else:
        print ("Coordinates are NOT in the D4 zone NFG area")
