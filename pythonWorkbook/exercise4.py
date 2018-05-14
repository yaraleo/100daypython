##
#Area of Field
#
SQFT_PER_ACRE = 43560
width = float(raw_input("Please enter width in feet "))
length = float(raw_input("Please enter length in feet "))
square = width * length / SQFT_PER_ACRE
#Display the result
print " the square is %d in acres" % square
