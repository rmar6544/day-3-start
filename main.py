#age, and rollercoaster height requirments 
#ask height is equall or greater than 120cm can ride 
#otherwise can not ride.
#ask if age is less than 12 amount $5.00
#age is greater than 12 but less than 18 amount $7.00
#if age is anything else amount $12.00

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
   print("You are tall enough to ride.")
   if age <= 12:
     print("Admission is $5.00")   
   elif age > 12 and age < 18:
     print("Admission is $7.00")  
   else:
     print("Admission is $12.00")  

else:
  print("I'm sorry you must be taller to ride.")  
