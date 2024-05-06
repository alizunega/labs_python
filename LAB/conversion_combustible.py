def liters_100km_to_miles_gallon(liters):
   miles = float((3.785411784 * (100 /liters))/1.609344)
   return miles

def miles_gallon_to_liters_100km(miles):
    liters = float(100/((miles * 1.609344)/3.785411784))
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


##60.31143162393162
##31.36194444444444
##23.52145833333333
##3.9007393587617467
##7.490910297239916
##10.009131205673757
