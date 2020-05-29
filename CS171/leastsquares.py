#Robert Roche
#CS171-Lecture A : Lab 062

#Leastsquares uses linear regression to analyze data and predict future results based off the data.
#Results with many decimal places were rounded off to 5 decimal places.


import math							#importing math and sys functions
import sys

print("Welcome to Linear Regression Generator.")		#opening message and prompt for file name
file_name = input("Enter the file name containing the data: ")
try:								#tries to execute code
	file = open(file_name)					#if file is not found the message is displayed and the program is exited.

except FileNotFoundError:
	print("Error: File could not be opened.")
	sys.exit()



x=[]								#creating x and y value lists
y=[]
error = []

with open(file_name,'r') as f:					
	for line in f:
		x.append(line.split(',', 1)[0])			#reading in the 1st entries into the x list
		y.append(line.split(',', 1)[1])			#second entries are read into y list

header1 = x[0]							#these statements assign the headers to string variables
header2 = y[0].strip('\n')					#gets rid of '\n' in each string variable

x.pop(0)							#these statements eliminate head values from the list
y.pop(0)
try:
	x = [float(e) for e in x]					#lists converted to float for calculations					
	y = [float(e) for e in y]
except ValueError:						#checks for bad input
	print("Error: Value or values in file could not be read!")
	sys.exit()

################################################		#calculates varibales for The linear Regression Line 

xa = sum(x)/len(x)						#declares variables based off provided formulas in pdf prompt
xi = x[len(x)-1]
ya = sum(y)/len(y)
yi = y[len(y)-1]
mnum=0
mdem=0
i=0
for element in x:						#this loop gets the numerator as per the formula provided
	mnum += (x[i]-xa)*(y[i]-ya)
	i+=1
i=0
for element in y:						#this loop gets the denominator as per the formula provided
	mdem += (x[i]-xa)**2
	i+=1
m = mnum/mdem
b=ya-(m*xa)
################################################		#calculates the average error
i=0
for element in x:
	error.append(abs(y[i]-(x[i]*m+b)))
	i+=1
error_avg = round(sum(error)/len(error),5)
################################################		#calculates the Regression Standard Error
reg_error = 0
i=0
for element in x:
	y2= x[i]*m + b
	reg_error+=(y[i]-y2)**2
	i+=1
reg_error = math.sqrt((reg_error*(1/(len(x)-2))))
################################################		#print all results together for neatness/ code readability
operator = ""
if b>0:								#simple formatting to handle if b is positive, negative, or 0
	operator = "+"
else: 
	operator = "-"
if b == 0:
	print("The linear Regression Line is y =",round(m,5),"*x")
else:
	print("The linear Regression Line is y =",round(m,5),"*x",operator,abs(round(b,5)))
print("Average Error for Known Values was +/-",error_avg)
print("Regression Standard Error for Known Values was",round(reg_error,5))
print("\nSystem ready to make predicitons.")

print("To quit type 'exit' as the year.")			#asks user for years to predict necessary outcome
year =""
while str(year)!="exit":					#keeps going as long as year is not exit
	year = input("Enter a year: ")
	if year == 'exit':
		break						#breaks loop if 'exit' is typed
	try:
		year = int(year)				#As long as entries are numbers, the code will work
		voters = year*m+b				
		print("Prediction when " + header1+" =",year,"is "+ header2 + " =",round(voters,5))

	except ValueError:					#if it is not a number and not 'exit', the error is displayed and the code loops again
		print("Input could not be understood please try again.")
		continue
	