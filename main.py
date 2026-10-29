#Kirjuta programm, mis küsib kasutajalt nime ja tervitab teda nimepidi.

#Algus 
#Küsi kasutajalt eesnime
#Salvesta väärtus muutujasse first_name
#Väljastab tervitust: "Hello, <eesnimi>!"
#Lõpp

first_name = input("Enter your first name:")
#print("Hello, " + first_name + "!")

last_name = input("Enter your last name::")


#f-string
print(f"Hello, {first_name} {last_name}!")

#tehke nii, et programm küsiks mitte ainult eesnime, vaid ka perekonnanime ning tervitaks teda nime ja perekonnanimega.

