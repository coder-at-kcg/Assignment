annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi- annual raise, as a decimal:"))
down_payment = total_cost * 0.25
current_saving = 0
monthly_salary=annual_salary/12
months = 0
r=0.04

while current_saving <= down_payment:
    if months % 6 ==0:
         annual_salary = annual_salary+(annual_salary*semi_annual_raise)
         current_saving = (current_saving * r/12) +( annual_salary/12* portion_saved) + current_saving
         months =months+1
    else:
         current_saving = current_saving * r/12 + annual_salary/12 * portion_saved + current_saving
         months =months+1
        
print(months)
