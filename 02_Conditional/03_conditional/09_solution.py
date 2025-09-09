year = 2022 

if (year % 400 == 0) or (year % 4 == 0 & year % 100 != 0):
  print(year, "That is leap year")
else:
  print(year, "that is not leap year")
