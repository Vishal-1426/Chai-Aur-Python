# from hello_chai import chai
# chai("vishal") 

chai = "Masala Chai"
print(chai.find("Chai"))

print(chai.find("chai"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

# String se list kese bnate hai

chai_type = "Masala"
quantity = 2
order = " I ordered {} cup of {} chai"
print(order.format(quantity, chai_type))

# list se string kese banti hai

chai_veriety = ["Lemon", "Masala", "ginger"]
print(" ".join(chai_veriety))

squared_num = [x**2 for x in range(10)]
print(squared_num)

cube_num = [y**3 for y in range(5)]
print(cube_num)

# EXAMPLE PRACTICE 1

chai_type = "Masala"
quantity = 3
order = " I ordered {} cup of {} chai"
print(order.format(quantity, chai_type))

# EXAMPLE PRACTICE 2

apple_type = "Apple"
quantity = "1kg"
order = " I ordered {} Apple"
print(order.format(quantity, apple_type))

#  EXAMPLE 1 CONVET STRING TO LIST 

imploy = "Hiring"
quantity = 5
order = " I have {} more imploy {}"
print(order.format(quantity, imploy))

#  EXAMPLE 2 CONVERT STRING TO LIST

golu = "Lemon"
quantity = 4
order = " i have {} cup of {} chai"
print(order.format(quantity, golu))

#  exapmle convert string to list 

bacchi = "Green"
quantity = 2
order = " i have {} cup of {} Tea"
print(order.format(quantity, bacchi))

#  EXAMPLE CONVERT STRING TO LIST 

date = "Banana"
quantity = 12
order = " i have {} {}"
print(order.format(quantity, date))

# EXAMPLE 3 CONVERT LIST TO STRING

vishal = ["Lemon", "anuj", "ayush"]
print(" ".join(vishal))

# EXAMPLE 4 CONVERT STRING TO LIST 
vishal = ["goku", "vishal", "moti"]
print(" ".join(vishal))

# EXAMPLE 5 CONVERT LIST TO STRING

ayush = ["vishal", "golu", "bacchi"]
print(" ".join(ayush))

parul = ["manu", "anshika"  , "moti"]
print(" ".join(parul))