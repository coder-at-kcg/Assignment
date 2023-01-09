total_cost = int(input("Enter House cost :"))
annual_salary = int(input("Enter annual Salary :"))
portion_save = float(input("Enter Portion saved [in decimal]:"))
r= float(input("Annual Raise [in decimal] :"))

down_payment = total_cost*0.25
current_saving = 0
monthly_salary = annual_salary/12
portion_save = portion_save*monthly_salary
months = 0

while True:
    if current_saving<=down_payment:
        current_saving = current_saving + portion_save + (current_saving*r/12) 
        months= months+1
    else:
        break
    
print(months)
