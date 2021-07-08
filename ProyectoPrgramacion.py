print("1. Tarapacá")
print("2. Antofagasta")
print("3. Atacama")
print("4. Coquimbo")
print("5. Valparaiso")
print("6. O'Higgins")
print("7. Maule")
print("8. Biobío")
print("9. Araucanía")
print("10. Los Lagos")
print("11. Aysén")
print("12. Magallanes")
print("13. Metropolitana")
print("14. Los Ríos")
print("15. Arica y Parinacota")
# Muestra las Regiones 

regiones = input("Ingrese el número o nombre de la Region que desee: ")
while regiones.isnumeric()!= True or int(regiones) > 15 :
    print("Ese no es un número o nombre de Region")
    regiones = input("Ingrese el número o nombre de la Region:")
regiones = int(regiones)

if regiones == 1 : #Muestra la Informacion de la Region de Tarapacá
    print("Tarapacá tiene una poblacion de 382773 personas en 7 comunas")
    lista_comtarapaca = ["1. Alto Hospicio","2. Camina","3. Colchane","4. Huara","5. Iquique", "6. Pica","7. Pozo almonte"]
    print(lista_comtarapaca)
    num =input("Escoja una Comuna de Tarapacá:")
    while num.isnumeric() == False or int(num) > 7:
        print("Ese no es un numero de alguna comuna de Tarapacá")
        num = input("Ingrese nuevamente un numero de comuna:")
    num = int(num)
    if num == 1:
        print("1")
    elif num == 2:
        print("2")
    elif num == 3:
        print("3")
    elif num == 4:
        print("4")
    elif num == 5:
        print("5")
    elif num == 6:
        print("6")
    else:
        print("7")


elif regiones == 2:
    print("2")
elif regiones == 3:
    print("3")
elif regiones == 4:
    print("4")
elif regiones == 5:
    print("5")
elif regiones == 6:
    print("6")
elif regiones == 7:
    print("7")
elif regiones == 8:
    print("8")
elif regiones == 9:
    print("9")
elif regiones == 10:
    print("10")
elif regiones == 11:
    print("11")
elif regiones == 12:
    print("12")
elif regiones == 13:
    print("13")
elif regiones == 14:
    print("14")
else:
    print("15")