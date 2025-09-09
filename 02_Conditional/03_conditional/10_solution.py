# Pet Food Recommandation
# Problem : Recommand a type of pet food based on the pet's species and age.(e.g..Dog: <2 years- puppy food, cat: > 5 years-senior cat)
  

species = input("Enter pet species (Dog/Cat): ")
age = int(input("Enter pet age in years: "))

if species == "Dog":
    if age < 2:
        print("Recommended food: Puppy food")
    elif age <= 7:
        print("Recommended food: Adult dog food")
    else:
        print("Recommended food: Senior dog food")

elif species == "Cat":
    if age < 2:
        print("Recommended food: Kitten food")
    elif age <= 5:
        print("Recommended food: Adult cat food")
    else:
        print("Recommended food: Senior cat food")

else:
    print("Sorry! Only Dog and Cat are supported.")



