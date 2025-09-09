  #  Dictionaries mein phele wali value ko change karke koii dusri value ko rakhne ka method

chai_types = {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
chai_types["Green"] = "Fresh"
print(chai_types) 

chai_types = {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
for chai in chai_types:
  print(chai)

  # YE DICTIONARIES MEIN VALUE OR KEY DONO KO PRINT KARNE KA SYNTEX 

for chai in chai_types:
  print(chai, chai_types[chai])

 