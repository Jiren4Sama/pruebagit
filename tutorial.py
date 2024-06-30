#Comentarios

#text1 ="zero is equal to "

#text2=0

#print(text1 + str(text2))

#show = "GOT"
#name1="Daniela"
#name2="Jon"
#name3="Tyrion"
#seasons = 8
#print(f"El show se llama {show} y tiene a los participantes {name1}, {name2} y {name3} en las {seasons} temporadas")

#INPUT
#print("Hola, Bienvenido al programa, llena el formulario")
#print("--------------------------------------------------------")
#name = input("Tu nombre:")
#edad = int(input("Edad:"))
#ciudad = input("Ciudad: ")
#email=input("Tu correo electronico:")

#print(f"Gracias {name}, tu edad es de {edad}, vives en {ciudad}, te enviamos la confirmacion al email {email}.")

#password = input("Crea una contrasena: ")

#print("Bienvenido al portal!!!")

#password_check=input("Entra tu contrasena: ")

#if password_check == password:
   # print("Enhorabuena, Bienvenido :)")

#else:
  #  print("Oh...no esa no era :(")

#print("Esto es un munijuego")
#number=int(input("Escoge un numero del 1-3:"))

#if number==1:
    #print("Eres el mejor")

#elif number==2:
   # print("Sigue intentando")

#elif number==3:
    #print("Una vez mas")
#else:
   # print("Eso no se puede bro....")

#NESTED CONDITIONAL

#print("Bienvenido a este videojuego")

#number = int(input("Escoge un numero entre 1-3:"))

#if number == 1:
    #print("Eres el mejor haciendo esto")
    #number2=float(input("Entra un numero decimal entre 1 y 2:"))

    #if number2 == 2.00:
        #print("Okay un poco menos que eso ")
    #elif number< 1.50:
        #print("Mas alto brother")

    #else:
        #print("Sabes que olvidalo")


#elif number == 2:
   # print("Estás solo, ¿verdad?")

#elif number == 3:
    #print("Emmm, no sé qué poner")

#else:
    #print("No sabes seguir instrucciones")

#x=0
#while x <=10:
      
    #print(x)

    #x=x+1
""""
my_number=19
guess = 0
max_guess=3

while guess< max_guess:
    number = int(input("Guess the number:"))
    guess +=1

    if number == my_number:
        print("WOW!Eres inteligente")
        break
    else:
        print("Try Again")


else:
 print("You ran out of chances")
 """

#for char in "Loops":
  #  print(char)

#for char in["I","Love","Programming"]:
   # print(char)


#for number in range(20):
  # print(number)

#for number in range(10,20):
   #print(number)

#SIntaxis es numeros del rango y al final  de cuanto en cuanto saltara el numero
#for number in range(10,20,2):
    #print(number)


"""
prices =[5,10,15,20,25]
total=0

for item in prices:
    total+=item


print(f"Your total price is: ${total}")
"""
#NESTED LOOPS


"""
for a in range(3):
    for b in range(3):
        for c in range(3):
            print(f"({a},{b},{c})")

"""
#True or false
"""
age = 28
is_working = True
is_married = False
has_criminal_record = True
if has_criminal_record != True:
    print("Eres elegible para el prestamo")

else:

    print("Lo siento, no es elegible para un prestamo")
"""

"""
print("Welcome to our online eligibility checker!")
print("---------------------------------------------")

age = int(input("Enter your age: "))
has_license = input("Do you have a license? [Y/N]: ").lower()

if has_license == "y":
    has_license = True
else:
    has_license = False

if age <= 35:
    print("The age is right!")
    
    if has_license:
        print("You have a valid license.")
        salary = int(input("Your monthly salary: $"))
        
        if salary >= 3500:
            print("Perfect! You are eligible.")
        else:
            print("I'm sorry, you are below our minimum requirements.")
    else:
        print("Sorry, we need to have a valid license.")
else:
    print("You don't have the age to do this.")
    """


# // divsion que redondea al entero solamente Ej. 1.787878 a 1
#round() redonde al entero Ej. 1.78787878 a 2
#** exponienciacion Ej: 2**3 = 8


#Programa de ejemplo






"""
print("Elegibility Checker 101")
name=input("Please enter your name:")
age=int(input("Enter your age:"))
salary=int(input("Enter Month Salary:"))
min_salary = 5000
has_good_credit=True

if salary >= min_salary and has_good_credit:
    print(f"Congratulations {name}, You are eligible for a mortgage.")
else:
    print(f"{name},it appears you may not be eligible at this time")
    """

#List,Turples, and Dictionaries

#friends =["Joey","Charlie","Monica","Ross","Kevin","Rachel"]

#print(len(friends))
"""
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
"""
#print(friends[-1])
#Rachel
#print(friends[-2])
#Kevin

#Las ultimas tres entradas
#print(friends[3:])

#print(friends[2:5])

#friends[5]="Anthony"
#print(friends) 

#METODOS
"""
numbers=[99,123,2313,1,1231411,343,435345]
numbers.insert(2,999)
numbers.sort()
print(numbers)
"""

#Turples 
#No se pueden cambiar ni modificar
#numbers = (1,2,3,4,5)

#Dictionaries

friends={
"name": "James",

"age":30,

"email":"aalksdnmakols@gmail.com",

"car":"Texta T1"



}
print(friends["name"])