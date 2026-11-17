
basic_salary = 50000

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da

print("===== Employee Salary Calculator =====")
print("Basic Salary  : Rs.", basic_salary)
print("HRA (20%)     : Rs.", hra)
print("DA (10%)      : Rs.", da)
print("--------------------------------------")
print("Gross Salary  : Rs.", gross_salary)
print("--------------------------------------")