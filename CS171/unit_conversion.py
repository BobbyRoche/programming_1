#Robert Roche
#Lab Section: 062

units = {									#this is the dictionary containing all of the necessary conveersions for each unit
	'inches': 1/2.54,
	'feet': (1 / 2.54) / 12,						#if you observe the values for each key, you will notice centimeters is the base unit
	'yards': ((1 / 2.54) / 12) / 3,
	'miles':(((1 / 2.54) / 12) / 3) / 1760,		
	'leagues':((((1 / 2.54) / 12) / 3) / 1760) / 3,				#all units are converted back to centimeters and then converted to the requested unit
	'decimeters': 10,
	'centimeters': 1,
	'meters': 1/100,
	'decameters':1/1000,
	'hectometers': 1/10000,
	'kilometers':1/100000
	}



print('\nWelcome to the length conversion wizard.')				#introductory output, a for loop is used to print out only the keys of the dictionary line by line
print('This program can convert between the following lengths.\n')

for unit in units:
	print (unit)
try:										#Error handling procedure in case a number is not entered
	length = float(input('\nEnter the length: \n'))				#this line gets the floating point length of the unit  they wish to convert

	print('\n(Units must be typed exactly as above, all lower case!)\n')
	unit1 = input('Enter the unit you are converting from: \n')		#this block prompts the user for two units of measurement, the original, and what they wish to convert it to
	unit2 = input('Enter the unit you are converting to: \n')

	try:									#error handling in case the value is not a key
		length2 = length/units[unit1]					#this block converts the unit back to centimeters, and then converts the centimeters to the desired unit
		length2 = length2 * units[unit2]

		print('\nThere are',round(length2,12),unit2,'in', length, unit1+'.' )	#prints the result

	except KeyError:							#if it is not a key the message is printed
			print('\nERROR: Unit(s) typed incorrectly, or non-existent!')
except ValueError:								#if it is not a number the message printed
	print('\nERROR: Wrong type, must be a number!')