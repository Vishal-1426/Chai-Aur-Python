#  Grade Calculator
#  Problem: Assign a letter grade based on a student's score:A(90-100),B(80-89), C(70-99), D(60-69), F(below 60).

score = 101
if score >= 101:
  print("Please verify your grade agin")
  exit()

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
print("Grade", grade) 


  

  
   
    