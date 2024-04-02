import random
people = []
for x in range(0,8):
         x = input("Enter the names of person: ")
         people.append(x)

index =  random.randint(0,7)
random_person = people[index]
print("Picking a random person: ",random_person)
         
         
