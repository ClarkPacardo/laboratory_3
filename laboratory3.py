salary = float(input("Enter your Monthly Salary: "))
loan = float(input("Enter the requested Loan amount: "))

if salary >= 30000.00 and loan <= salary * 10:
    print("You are Eligible for loan")
    months= int(input("Enter the number of months the customer wish to pay: "))
    interest = 0.10
    total = loan + (loan*interest)
    monthly_payment = total/months
    print("Total amount of payment "+str(total))
    print("Total payment over "+str(months)+" months: "+str(monthly_payment))
else:
    print("You are not eligible for a loan")
    if salary < 30000:
        print("You are not eligible for a loan; Monthly salary is less than 30,000")
    if loan >= 10 * salary:
        print("You are not eligible for a loan; Loan amount exceeds 10 times your salary.")

