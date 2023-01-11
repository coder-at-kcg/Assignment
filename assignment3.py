annual_salary = int(input("Enter annual Salary :"))
semi_annual_raise = 0.07
r=0.04
house = 1000000
down_pay = house*0.25

monthly_salary=annual_salary/12

annual_salaryhike= annual_salary+(annual_salary*semi_annual_raise)
monthly_salaryhike = annual_salaryhike/12

a= monthly_salary
b= monthly_salaryhike   

total_salary = (30*a)+(6*b)          #[in 36 months,the semi_annual_raise occurs 6 times. So 30 months normal salary and 6months hiked salary ]
portion_save = (down_pay)/(total_salary)
print(portion_save)
        
