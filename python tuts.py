num_str = input("Input rods:")
num_float = float(num_str)
x = num_float * 5.0292
y = x / 0.3048
z = x /1609.34
a = num_float/ 40
b = 0.06/ num_float
print("Conversions \nMeters:", round(x, 3), "\nFeet: ", round(y, 3),"\nMiles:", round(z, 3),"\nFurlongs: ",round(a,3),"\nMinutes to walk",num_float, "rods:",round(b, 3))


#Unit of conversion

'''
1 rod = 5.0292 meters
1 furlong = 40 rods
1 mile = 1609.34 meters
1 foot = 0.3048 meters
average walking speed is 3.1 miles per hour 
'''