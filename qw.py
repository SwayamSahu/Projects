
'''x = ["ram","charan","dev","lonty"]
name = input("enter your name: ")
x.append(name)
print(x)'''



'''month = ("January","February","March","April","May","June","July","August","September","October","November","December")
x = input("type your birthday in the format DD-MM-YYYY: ")

y = int(x[3:5])-1
bd_mon = month[y] ;;;;;;;;;;;;;

print("You were born in", bd_mon)


person = {"name": "pimpudi", "gender": "female", "age": "60","address": "chandini","phone": "124421"}

key = input("what info u wan to know about the person? ").lower()
x = person.get(key,"invalid input")

print(x)'''


x = 23

y = int(input("enter your age: "))

if x>y:
    print("He's younger than you")
elif x<y:
    print("He's older than you")
else:
    print("you two have same age")
