#RobertRoche
#CS171-A(lecture)
#CS171-062

print("\nWelcome to the Student Loan Calculator")#principle loan, or the original amount taken out

p= int (input("Enter the amount of the loan in dollars with (no commas):\n")) #prompts user to enter principle loan, or the original amount taken out
								    	    #this value is stored in 'p'
y= int(input("Enter the number of years the loan is for:\n"))		    #prompts the user for the number of years the loan is being paid off in, and stores this value in 'y'.

t = 12									    #t is the amount of times the interest is compounded a year in this case it is 12 times or once per month.

i = 0.034								    #i is the interest rate of the loan.

f = 0.01051								    #f is the fee rate for the loan.

M = (p*i)/(12*(1-(1+i/t)**(-y*t)))					    #M is the monthly payment of the loan, this is calculated by the formula provided in the instructions.
b = M*t*y								    #b is the balance due, or the total after the principle, interest, and fees are all accounted for.
interestPaid = b-p							    # interestPaid stores the total amount of interest the student pays over the course of the loan payment.
feePaid = p*f								    #feePaid stores the total additional fees that are paid throughout the course of the loan payment.
cost = interestPaid+feePaid						    #cost is essentially the loss after all debt is paid. The cost is the excess amount you paid on the loan, in other words
									    #it is how much the loan cost the student.
print("____________________________________________________")		    #The following chunks of code print the data that was collected and calculated and displays the results.


print("Subsidized Federal Direct Loan")
print("Principle:",p)
print("Interest Rate:",round(i*100,2))
print("Years:",y)
print("Monthly Payment:",round(M,2))
print("Total Paid on Loan:",round(b,2))
print("Total Interest Paid:",round(interestPaid,2))
print("Additional Fees Paid:",round(feePaid,2))
print("Total Costs Over Principle:",round(cost,2))

i = 0.068								    #The interest rate is adjusted for unsubsidized loans, and the principle is adjusted to account for the
									    #four additional years the student will be paying the loan during college.
f = 0.01051								    

p2 = p * (1+i*4.25)

M = (p2*i)/(12*(1-(1+i/t)**(-y*t)))
b = M*t*y
interestPaid = b-p
feePaid = p*f
cost = interestPaid+feePaid

print("____________________________________________________")		    #The print block is then repeated with the adjusted data.


print("Unsubsidized Federal Direct Loan")
print("Principle:",p)
print("Interest Rate:",round(i*100,2))
print("Years:",y)
print("Monthly Payment:",round(M,2))
print("Total Paid on Loan:",round(b,2))
print("Total Interest Paid:",round(interestPaid,2))
print("Additional Fees Paid:",round(feePaid,2))
print("Total Costs Over Principle:",round(cost,2))

i = 0.079								    #The interest rate and fee rate are again adjusted to the PLUS loan while maintaining the unsubsizided loan format.									

f = 0.04204

p2 = p * (1+i*4.25)

M = (p2*i)/(12*(1-(1+i/t)**(-y*t)))
b = M*t*y
interestPaid = b-p
feePaid = p*f
cost = interestPaid+feePaid

print("____________________________________________________")		    #The print block is then repeated with the adjusted data.	  


print("Federal Plus Loan")
print("Principle:",p)
print("Interest Rate:",round(i*100,2))
print("Years:",y)
print("Monthly Payment:",round(M,2))
print("Total Paid on Loan:",round(b,2))
print("Total Interest Paid:",round(interestPaid,2))
print("Additional Fees Paid:",round(feePaid,2))
print("Total Costs Over Principle:",round(cost,2))