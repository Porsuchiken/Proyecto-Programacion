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
        print("Poblacion = 129999 personas")
    elif num == 2:
        print("Poblacion = 1375 personas")
    elif num == 3:
        print("Poblacion = 1583 personas")
    elif num == 4:
        print("Poblacion = 3000 personas")
    elif num == 5:
        print("Poblacion = 223463 personas")
    elif num == 6:
        print("Poblacion = 5958 personas")
    else:
        print("Poblacion = 17395 personas")


elif regiones == 2:#Muestra la informacion de la Region de Antofagasta
    print("Antofagasta tiene una poblacion de 691854 personas en 9 comunas")
    lista_comantofagasta = ["1. Antofagasta","2. Calama","3. Maria Elena","4. Mejillones","5. Ollague", "6. San Pedro de Atacama",
    "7. Sierra Gordam","8. Taltal","9.Tocopilla"]
    print(lista_comantofagasta)
    num2 =input("Escoja una Comuna de Antofagasta:")
    while num2.isnumeric() == False or int(num2) > 9:
        print("Ese no es un numero de alguna comuna de Antofagasta")
        num2 = input("Ingrese nuevamente un numero de comuna:")
    num2 = int(num2)
    if num2 == 1:
        print("Poblacion = 	425725 personas")
    elif num2 == 2:
        print("Poblacion = 190336 personas")
    elif num2 == 3:
        print("Poblacion = 6814 personas")
    elif num2 == 4:
        print("Poblacion = 14776 personas")
    elif num2 == 5:
        print("Poblacion = 287 personas")
    elif num2 == 6:
        print("Poblacion = 10434 personas")
    elif num2 == 7:
        print("Poblacion = 1746 personas")
    elif num2 == 8:
        print("Poblacion = 13657 personas")
    else: 
        print("Poblacion = 28079 personas")


elif regiones == 3:
    print("Atacama tiene una poblacion de 314709 personas en 9 comunas")
    lista_comatacama = ["1. Alto  del Carmen","2. Caldera","3. Chanaral","4. Copiapo","5. Diego de Almagro", "6. Freirina,",
    "7. Huasco","8. Tierra amarilla","9.Vallenar"]
    print(lista_comatacama)
    num3 =input("Escoja una Comuna de Atacama:")
    while num3.isnumeric() == False or int(num3) > 9:
        print("Ese no es un numero de alguna comuna de Atacama")
        num3 = input("Ingrese nuevamente un numero de comuna:")
    num3 = int(num3)
    if num3 == 1:
        print("Poblacion = 	5729 personas")
    elif num3 == 2:
        print("Poblacion = 19426 personas")
    elif num3 == 3:
        print("Poblacion = 13164 personas")
    elif num3 == 4:
        print("Poblacion = 171766 personas")
    elif num3 == 5:
        print("Poblacion = 14358 personas")
    elif num3 == 6:
        print("Poblacion = 7681 personas")
    elif num3 == 7:
        print("Poblacion = 11264 personas")
    elif num3 == 8:
        print("Poblacion = 14312 personas")
    else: 
        print("Poblacion = 57009 personas")



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