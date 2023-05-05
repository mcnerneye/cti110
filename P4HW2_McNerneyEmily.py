#CTI-110
#P4HW2 - Salary Calculator
#Emily McNerney
#April 24, 2023
#

# set global variables
numOfEmp = 0  # holds total employees entered
totalOverTimePay = 0  # holds total over time pay for all employees
totalRegPay = 0  # holds total regular pay for all employees
totalGrossPay = 0  # holds total gross pay for all employees

# now, run a loop until user wishes to exit
while True:

    # in each iteration, enter employee's name, hours worked, and pay rate
    name = input("Enter employee's name or \"Done\" to terminate: ")

    # check if name is "Done", then break the loop without any further user input
    if name == "Done":
        break
    else:

        # if correct name then increase employee count by 1
        numOfEmp += 1

    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What did " + name + "\' pay rate? "))

    # now, for this employee, set variables to calculate values
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0

    # now, check for overtime, if number of worked hours are greater than 40
    if hours > 40:

        # then calculate overtime
        overtime = hours - 40

        # calculate over time Pay(50% more)
        overtimePay = overtime * rate * 1.5

        # calculate regular pay
        regularPay = 40 * rate

        # calculate gross Pay
        grossPay = regularPay + overtimePay
    else:

        # otherwise, simply calculate regular Pay and gross pay
        regularPay = hours * rate
        grossPay = regularPay

    # then, add over time pay to total over time pay
    totalOverTimePay += overtimePay

    # add regular pay to total regular pay
    totalRegPay += regularPay

    # add gross pay to total gross pay
    totalGrossPay += grossPay

    # then, print employee name
    print("\nEmployee name: " + name + "\n")

    # and then print all the abover calculate values in tabular format as per the given format
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay",
                                                        "RegHour Pay", "Gross Pay"))
    print(
        "-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overtimePay,
                                                                            regularPay, grossPay))
    print()

# once the loop terminates, print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Total number of employees entered:", numOfEmp)
print("Total amount payed for over time: $" + '{:.2f}'.format(totalOverTimePay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount payed in gross: $" + '{:.2f}'.format(totalGrossPay))
