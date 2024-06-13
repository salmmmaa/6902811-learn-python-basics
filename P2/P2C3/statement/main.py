def monthly_salary(annual_salary):
    return annual_salary / 12
def weekly_salary(monthly_salary):
    return monthly_salary / 4
def hourly_wage(weekly_salary, hours_worked):
    return weekly_salary / hours_worked


def main():
    annual_salary = float(input("Enter your annual salary : "))
    hours_worked = float(input("Enter the number of hours worked per week : "))
    monthly = monthly_salary(annual_salary)
    weekly = weekly_salary(monthly)
    hourly = hourly_wage(weekly, hours_worked)

    print("Your hourly wage is",  hourly, "euros.")

if __name__ == "__main__":
    main()
