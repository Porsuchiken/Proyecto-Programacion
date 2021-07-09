from numpy import vdot


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
print("16. Nuble")
# Muestra las Regiones 

regiones = input("Ingrese el número la Region que desee: ")
while regiones.isnumeric()!= True or int(regiones) > 16 :
    print("Ese no es un número Region")
    regiones = input("Ingrese el número de la Region:")
regiones = int(regiones)

if regiones == 1 : #Muestra la Informacion de la Region de Tarapacá
    print("Tarapacá tiene una poblacion de 382773 personas en 7 comunas")
    lista_comtarapaca = ["1. Alto Hospicio","2. Camina","3. Colchane","4. Huara","5. Iquique", "6. Pica","7. Pozo almonte"]
    print(lista_comtarapaca)
    num =input("Escoja un numero de las Comunas de Tarapacá:")
    while num.isnumeric() == False or int(num) > 7:
        print("Ese no es un numero de alguna comuna de Tarapacá")
        num = input("Ingrese nuevamente un numero de comuna:")
    num = int(num)
    if num == 1:
        print("Poblacion = 129999 personas")
        import matplotlib.pyplot as plt
        ejex=[8,8,7,15,19,27]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 2:
        print("Poblacion = 1375 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 3:
        print("Poblacion = 1583 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 4:
        print("Poblacion = 3000 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 5:
        print("Poblacion = 223463 personas")
        import matplotlib.pyplot as plt
        ejex=[11,8,10,10,29,38]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 6:
        print("Poblacion = 5958 personas")    
        import matplotlib.pyplot as plt
        ejex=[9,17,21,17,13,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 17395 personas")
        import matplotlib.pyplot as plt
        ejex=[2,2,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 2:#Muestra la informacion de la Region de Antofagasta
    print("Antofagasta tiene una poblacion de 691854 personas en 9 comunas")
    lista_comantofagasta = ["1. Antofagasta","2. Calama","3. Maria Elena","4. Mejillones","5. Ollague", "6. San Pedro de Atacama",
    "7. Sierra Gordam","8. Taltal","9.Tocopilla"]
    print(lista_comantofagasta)
    num2 =input("Escoja un numero de las Comunas de Antofagasta:")
    while num2.isnumeric() == False or int(num2) > 9:
        print("Ese no es un numero de alguna comuna de Antofagasta")
        num2 = input("Ingrese nuevamente un numero de comuna:")
    num2 = int(num2)
    if num2 == 1:
        print("Poblacion = 	425725 personas")
        import matplotlib.pyplot as plt
        ejex=[49,54,62,86,121,140]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 2:
        print("Poblacion = 190336 personas")
        import matplotlib.pyplot as plt
        ejex=[12,11,10,10,9,25]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 3:
        print("Poblacion = 6814 personas")
        import matplotlib.pyplot as plt
        ejex=[1,2,4,6,7,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 4:
        print("Poblacion = 14776 personas")
        import matplotlib.pyplot as plt
        ejex=[11,13,14,18,30,38]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 5:
        print("Poblacion = 287 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 6:
        print("Poblacion = 10434 personas")
        import matplotlib.pyplot as plt
        ejex=[1,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 7:
        print("Poblacion = 1746 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 8:
        print("Poblacion = 13657 personas")
        import matplotlib.pyplot as plt
        ejex=[3,5,5,5,4,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else: 
        print("Poblacion = 28079 personas")
        import matplotlib.pyplot as plt
        ejex=[1,3,8,4,1,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 3:
    print("Atacama tiene una poblacion de 314709 personas en 9 comunas")
    lista_comatacama = ["1. Alto  del Carmen","2. Caldera","3. Chanaral","4. Copiapo","5. Diego de Almagro", "6. Freirina,",
    "7. Huasco","8. Tierra amarilla","9.Vallenar"]
    print(lista_comatacama)
    num3 =input("Escoja un numero de las Comunas de Atacama:")
    while num3.isnumeric() == False or int(num3) > 9:
        print("Ese no es un numero de alguna comuna de Atacama")
        num3 = input("Ingrese nuevamente un numero de comuna:")
    num3 = int(num3)
    if num3 == 1:
        print("Poblacion = 	5729 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 2:
        print("Poblacion = 19426 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 3:
        print("Poblacion = 13164 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 4:
        print("Poblacion = 171766 personas")
        import matplotlib.pyplot as plt
        ejex=[5,5,5,4,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 5:
        print("Poblacion = 14358 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 6:
        print("Poblacion = 7681 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 7:
        print("Poblacion = 11264 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,1,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 8:
        print("Poblacion = 14312 personas")
        import matplotlib.pyplot as plt
        ejex=[4,4,4,2,0,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else: 
        print("Poblacion = 57009 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,7,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 4:
    print("Coquimbo tiene una poblacion de 836096 personas en 15 comunas")
    lista_comcoquimbo = ["1. Andacollo","2. Canela","3. Combarbala","4. Coquimbo","5. Illapel", "6. La Higuera,",
    "7. La Serena","8. Los Vilos","9. Monte Patria","10. Ovalle", "11. Paiguano", "12. Punitaqui","13. Rio Hurtado","14. Salamanca",
    "15. Vicuna"]
    print(lista_comcoquimbo)
    num4 =input("Escoja un numero de las Comunas de Coquimbo:")
    while num4.isnumeric() == False or int(num4) > 15:
        print("Ese no es un numero de alguna comuna de Coquimbo")
        num4 = input("Ingrese nuevamente un numero de comuna:")
    num4 = int(num4)
    if num4 == 1:
        print("Poblacion = 	11791 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 2:
        print("Poblacion =  9546 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 3:
        print("Poblacion =  13884 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 4:
        print("Poblacion =  256735 personas")
        import matplotlib.pyplot as plt
        ejex=[1,2,0,2,3,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 5:
        print("Poblacion = 32801 personas")
        import matplotlib.pyplot as plt
        ejex=[13,12,10,7,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 6:
        print("Poblacion =  4450 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 7:
        print("Poblacion = 249656 personas")
        import matplotlib.pyplot as plt
        ejex=[2,1,1,2,4,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 8:
        print("Poblacion =  23374 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 9 :
        print("Poblacion = 	32527 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 10 :
        print("Poblacion =  121269 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 11 :
        print("Poblacion =  4675 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 12 :
        print("Poblacion =  12165 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,1,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 13 :
        print("Poblacion =  4372 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 14 :
        print("Poblacion =  29110 personas")
        import matplotlib.pyplot as plt
        ejex=[3,3,3,3,1,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  29741 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 5:
    print("Valparaiso tiene una poblacion de 1960170 personas en 38 comunas")
    lista_comvalparaiso  = ["1. Algarrobo","2. Cabildo","3. Calera","4. Calle Larga","5. Cartagena", "6. Casa Blanca,",
    "7. Catemu","8. Concon","9. El Quisco","10. El Tabo", "11. Hijuelas", "12. Isala de Pascua","13. Juan Fernandez","14. La Cruz",
    "15. La Ligua", "16. Limache","17. Llaillay","18. Los Andes", "19. Nogales", "20. Olmue","21. Panquehue","22. Papudo","23.Petorca",
    "24. Punchucavi","25. Putaendo", "26. Quillota","27. Quilpue","28. Quintero","29. Rinconada","30. San Antonio","31. San Sebastian",
    "32. San Felipe","33. Santa Maria","34. Santo Domingo","35. Valparaiso","36. Villa Alemana","37. Viña del Mar","38. Zapallar"]
    print(lista_comvalparaiso)
    num5 =input("Escoja un numero de las Comunas de Valparaiso:")
    while num5.isnumeric() == False or int(num5) > 38:
        print("Ese no es un numero de alguna comuna de Valparaiso")
        num5 = input("Ingrese nuevamente un numero de comuna:")
    num5 = int(num5)
    if num5 == 1:
        print("Poblacion = 	15174 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 2:
        print("Poblacion =  20663 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,1,0,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 3:
        print("Poblacion =  53591 personas")
        import matplotlib.pyplot as plt
        ejex=[1,3,5,6,9,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 4:
        print("Poblacion =  16482 personas")
        import matplotlib.pyplot as plt
        ejex=[2,2,3,4,2,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 5:
        print("Poblacion =  25357 personas")
        import matplotlib.pyplot as plt
        ejex=[2,2,0,0,4,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 6:
        print("Poblacion =  29170 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 7:
        print("Poblacion =  15213 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 8:
        print("Poblacion =  45889 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 9 :
        print("Poblacion = 	17742 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 10 :
        print("Poblacion =  14338 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 11 : 
        print("Poblacion =  19099 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 12 :
        print("Poblacion =  8277 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 13 :
        print("Poblacion =  1033 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 14 :
        print("Poblacion =  25321 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 15 :
        print("Poblacion =  37739 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 16 :
        print("Poblacion =  49931 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 17 :
        print("Poblacion =  26533 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 18 :
        print("Poblacion =  68093 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 19 :
        print("Poblacion =  23490 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 20 :
        print("Poblacion =  19266 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 21 :
        print("Poblacion =  7633 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 22 :
        print("Poblacion =  6201 ersonas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 23 :
        print("Poblacion =  10558 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 24 :
        print("Poblacion =  20071 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 25 :
        print("Poblacion =  17645 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 26 :
        print("Poblacion =  97572 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 27 :
        print("Poblacion =  167085 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 28 :
        print("Poblacion =  36135 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 29 :
        print("Poblacion =  11263 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 30 :
        print("Poblacion =  96761 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 31 :
        print("Poblacion =  20643 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 32 :
        print("Poblacion =  83494 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 33 :
        print("Poblacion =  16367 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 34 :
        print("Poblacion =  11934 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 35 :
        print("Poblacion =  315732 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 36 :
        print("Poblacion =  139310 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 37 :
        print("Poblacion =  361371 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  7994 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 13:
    print("Metropolitana tiene una poblacion de 8125072 personas en 52 comunas")
    lista_commetropolitana  = ["1. Alhue","2. Buin","3. Calera","4. Calera de Tango","5. Cerrillos", "6. Cerro Navia,",
    "7. Colina","8. Conchali","9. Curacavi","10. El Bosque", "11. El Monte", "12. Estacion Central","13. Huechuraba","14. Independencia",
    "15. Isla de Maipo", "16. La Cisterna","17. La Florida","18. La Granja", "19. La Pintana", "20. La Reina","21. Lampa","22. Las Condes","23. Lo Barnechea",
    "24. Lo Espejo","25. Lo Prado", "26. Macul","27. Maipu","28. Maria Pinto","29. Melipilla","30. 	Nunoa","31. Padre Hurtado",
    "32. Paine","33. Pedro Aguirre Cerda","34. Penaflor","35. Penalolen","36. Pirque","36. Providencia","37. Pudahuel","38. Puente Alto","39. Quilicura",
    "40. Quinta Normal","41. Recoleta", "42. Renca", "43. San Bernardo", "44. San Joaquin", "45. San Jose de Maipo", "46. San Miguel",
    "47. San Pedro","48. San Ramon","49. Santiago","50.	Talagante","51. Tiltil","52. Vitacura"]
    print(lista_commetropolitana)
    num13 =input("Escoja un numero de las Comunas de Metropolitana:")
    while num13.isnumeric() == False or int(num13) > 52:
        print("Ese no es un numero de alguna comuna de Metropolitana")
        num13 = input("Ingrese nuevamente un numero de comuna:")
    num13 = int(num13)
    if num13 == 1:
        print("Poblacion =  7405 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 2:
        print("Poblacion =  109641 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 3:
        print("Poblacion =  28525 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 4:
        print("Poblacion =  88956 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 5:
        print("Poblacion =  142465 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 6:
        print("Poblacion =  180353 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 7:
        print("Poblacion =  139195 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 8:
        print("Poblacion =  36430 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 9 :
        print("Poblacion = 	172000 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 10 :
        print("Poblacion =  40014 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 11 : 
        print("Poblacion =  206792 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 12 :
        print("Poblacion =  112528 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 13 :
        print("Poblacion =  142065 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 14 :
        print("Poblacion =  40171 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 15 :
        print("Poblacion =  100434 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 16 :
        print("Poblacion =  402433 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 17 :
        print("Poblacion =  122557 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 18 :
        print("Poblacion =  189335 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 19 :
        print("Poblacion =  100252 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 20 :
        print("Poblacion =  126898 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 21 :
        print("Poblacion =  330759 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 22 :
        print("Poblacion =  124076 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.plot(ejex,ejey)
        plt.show()
    elif num13 == 23 :
        print("Poblacion =  103865 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 24 :
        print("Poblacion =  104403 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 25 :
        print("Poblacion =  134635 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 26 :
        print("Poblacion =  578605 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 27 :
        print("Poblacion =  14926 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 28 :
        print("Poblacion =  141612 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 29 :
        print("Poblacion =  250192 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 30 :
        print("Poblacion =  74188 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 31 :
        print("Poblacion =  82766 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 32 :
        print("Poblacion =  107803 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 33 :
        print("Poblacion =  101058 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 34 :
        print("Poblacion =  266798 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 35 :
        print("Poblacion =  30433 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 36 :
        print("Poblacion =  157749 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 37 :
        print("Poblacion =  253139 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 38 :
        print("Poblacion =  645909 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 39 :
        print("Poblacion =  254694 personas") 
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 40 :
        print("Poblacion =  136368 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 41 :
        print("Poblacion =  190075 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 42 :
        print("Poblacion =  160847 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 43 :
        print("Poblacion =  334836 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 44 :
        print("Poblacion =  103485 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 45 :
        print("Poblacion =  18644 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 46 :
        print("Poblacion =  133059 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 47 :
        print("Poblacion =  11953 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 48 :
        print("Poblacion =  86510 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 49 :
        print("Poblacion =  503147 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 50 :
        print("Poblacion =  81838 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 51 :
        print("Poblacion =  21477 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  96774 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 6:
    print("O'Higgins tiene una poblacion de 991063 personas en 33 comunas")
    lista_comhiggins  = ["1. Chepica","2. Chimbarongo","3. Codegua","4. Coinco","5. Coltauco", "6. Donihue",
    "7. Graneros","8. La Estrella","9. 	Las Cabras","10. Litueche", "11. Lolol", "12. Machali","13. Malloa","14. Marchihue",
    "15. Mostazal", "16. Nancagua","17. Navidad","18. Olivar", "19. Palmilla", "20. Paredones","21. Peralillo","22. Peumo","23. Pichidegua",
    "24. Pichilemu","25. Placilla", "26. Pumanque","27. Quinta de Tilcoco","28. Rancagua","29. Rengo","30. Requinoa","31. San Fernando",
    "32. San Vicente","33. Santa Cruz"]
    print(lista_comhiggins)
    num6 =input("Escoja un numero de las Comunas de O'Higgins:")
    while num6.isnumeric() == False or int(num6) > 33:
        print("Ese no es un numero de alguna comuna de O'Higgins")
        num6 = input("Ingrese nuevamente un numero de comuna:")
    num6 = int(num6)
    if num6 == 1:
        print("Poblacion =  15925 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 2:
        print("Poblacion =  37696 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 3:
        print("Poblacion =  14096 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 4:
        print("Poblacion =  7831 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 5:
        print("Poblacion =  21263 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 6:
        print("Poblacion =  22700 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 7:
        print("Poblacion =  36504 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 8:
        print("Poblacion =  3114 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 9 :
        print("Poblacion = 	26749 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 10 :
        print("Poblacion =  6765 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 11 : 
        print("Poblacion =  7289 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 12 :
        print("Poblacion =  59913 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 13 :
        print("Poblacion =  14163 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 14 :
        print("Poblacion =  7632 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 15 :
        print("Poblacion =  27462 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 16 :
        print("Poblacion =  19141 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 17 :
        print("Poblacion =  6904 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 18 :
        print("Poblacion =  14624 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 19 :
        print("Poblacion =  13299 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 20 :
        print("Poblacion =  6349 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 21 :
        print("Poblacion =  11848 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 22 :
        print("Poblacion =  14952 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 23 :
        print("Poblacion =  20743 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 24 :
        print("Poblacion =  17882 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 25 :
        print("Poblacion =  9164 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 26 :
        print("Poblacion =  3531 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 27 :
        print("Poblacion =  13877 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 28 :
        print("Poblacion =  265211 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 29 :
        print("Poblacion =  63710 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 30 :
        print("Poblacion =  30371 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 31 :
        print("Poblacion =  78642 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 ==32:
        print("Poblacion =  50617 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  41096 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 7:
    print("Maule tiene una poblacion de 1131939 personas en 30 comunas")
    lista_commaule  = ["1. Cauquenes","2. Chanco","3. Colbun","4. Constitucion","5.	Curepto", "6. Curico",
    "7. Empedrado","8. Hualane","9. Licanten","10. Linares", "11. Longavi", "12. Maule","13. Molina","14. Parral",
    "15. Pelarco", "16. Pelluhue","17. Pencahue","18. Rauco", "19. Retiro", "20. Rio Claro","21. Romeral","22. Sagrada Familia",
    "23. San Clemente","24. San Javier","25. San Rafael", "26. Talca","27. Teno","28. Vichuquen","29. Villa Alegre","30. Yerbas Buenas"]
    print(lista_commaule)
    num7 =input("Escoja un numero de las Comunas de Maule:")
    while num7.isnumeric() == False or int(num7) > 30:
        print("Ese no es un numero de alguna comuna de Maule")
        num7 = input("Ingrese nuevamente un numero de comuna:")
    num7 = int(num7)
    if num7 == 1:
        print("Poblacion =  44143 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 2:
        print("Poblacion =  9331 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.plot(ejex,ejey)
        plt.show()
    elif num7 == 3:
        print("Poblacion =  22565 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 4:
        print("Poblacion =  50348 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 5:
        print("Poblacion =  9426 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 6:
        print("Poblacion =  163626 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 7:
        print("Poblacion =  4206 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 8:
        print("Poblacion =  10222 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 9 :
        print("Poblacion = 	6989 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 10 :
        print("Poblacion =  101073 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 11 : 
        print("Poblacion =  32810 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 12 :
        print("Poblacion =  60000 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 13 :
        print("Poblacion =  49800 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 14 :
        print("Poblacion =  44544 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 15 :
        print("Poblacion =  9083 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 16 :
        print("Poblacion =  8092 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 17 :
        print("Poblacion =  8601 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 18 :
        print("Poblacion =  11248 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 19 :
        print("Poblacion =  21071 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 20 :
        print("Poblacion =  14753 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 21 :
        print("Poblacion =  16170 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 22 :
        print("Poblacion =  19469 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 23 :
        print("Poblacion =  46292 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 24 :
        print("Poblacion =  49451 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 25 :
        print("Poblacion =  9959 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 26 :
        print("Poblacion =  236724 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 27 :
        print("Poblacion =  30850  personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 28 :
        print("Poblacion =  4381 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 29 :
        print("Poblacion =  17512  personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  19200 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 16:
    print("Nuble tiene una poblacion de 511551 personas en 21 comunas")
    lista_comnuble  = ["1. Bulnes","2. Chillan","3. Chillan Viejo","4. Cobquecura","5. Coelemu", "6. Coihueco",
    "7. El Carmen","8.  Ninhue","9. Niquen","10. Pemuco", "11. Pinto", "12. Portezuelo","13. Quillon","14. Quirihue",
    "15. Ranquil", "16. San Carlos","17. San Fabian","18. San Ignacio", "19. San Nicolas", "20. Treguaco","21. Yungay"]
    print(lista_comnuble)
    num16 =input("Escoja un numero de las Comunas de Nuble:")
    while num16.isnumeric() == False or int(num16) > 21:
        print("Ese no es un numero de alguna comuna de Nuble")
        num16 = input("Ingrese nuevamente un numero de comuna:")
    num16 = int(num16)
    if num16 == 1:
        print("Poblacion = 22607 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 2:
        print("Poblacion = 198624 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 3:
        print("Poblacion = 33827 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 4:
        print("Poblacion = 5275 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 5:
        print("Poblacion = 	16845 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 6:
        print("Poblacion =  28375 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 7:
        print("Poblacion =  12334 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 8:
        print("Poblacion =  5414 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 9 :
        print("Poblacion = 	11567 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 10 :
        print("Poblacion =  8639 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 11 : 
        print("Poblacion =  11880 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 12 :
        print("Poblacion =  4940 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 13 :
        print("Poblacion =  18777 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 14 :
        print("Poblacion =  12192 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 15 :
        print("Poblacion =  6261 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 16 :
        print("Poblacion =  56252 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 17 :
        print("Poblacion =  4654 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 18 :
        print("Poblacion =  16624 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 19 :
        print("Poblacion =  12172 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 20 :
        print("Poblacion =  5696 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  18596 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 8:
    print("Biobio tiene una poblacion de 1663696 personas en 33 comunas")
    lista_combiobio  = ["1. Alto Biobio","2. Antuco","3. Arauco","4. Cabrero","5. Canete", "6. Chiguayante",
    "7. Concepcion","8. Contulmo","9. Coronel","10. Curanilahue", "11. Florida", "12.  Hualpen","13. Hualqui","14.  Laja",
    "15. Lebu", "16. Los Alamos","17. Los Angeles ","18. Lota ", "19. Mulchen", "20. Nacimiento","21. Negrete","22. Penco","23. Quilaco",
    "24. Quilleco","25. San Pedro de la Paz", "26. San Rosendo","27.  Santa Barbara","28.  Santa Juana","29. Talcahuano","30. 	Tirua","31. Tome",
    "32. Tucapel","33. Yumbel"]
    print(lista_combiobio)
    num8 =input("Escoja un numero de las Comunas del Biobio:")
    while num8.isnumeric() == False or int(num8) > 33:
        print("Ese no es un numero de alguna comuna de Biobio")
        num8 = input("Ingrese nuevamente un numero de comuna:")
    num8 = int(num8)
    if num8 == 1:
        print("Poblacion =  6775 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 2:
        print("Poblacion =  4306 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 3:
        print("Poblacion =  38679 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 4:
        print("Poblacion =  30725 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 5:
        print("Poblacion =  37003 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 6:
        print("Poblacion =  91180 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 7:
        print("Poblacion =  238092 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 8:
        print("Poblacion =  6330 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 9 :
        print("Poblacion = 	125829 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 10 :
        print("Poblacion =  33892 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 11 : 
        print("Poblacion =  11841 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 12 :
        print("Poblacion =  97273 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 13 :
        print("Poblacion =  26201 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 14 :
        print("Poblacion =  23873 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 15 :
        print("Poblacion =  27100 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 16 :
        print("Poblacion =  22524 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 17 :
        print("Poblacion =  218515 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 18 :
        print("Poblacion =  45750 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 19 :
        print("Poblacion =  31041 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 20 :
        print("Poblacion =  27944 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 21 :
        print("Poblacion =  10429 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 22 :
        print("Poblacion =  49865 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 23 :
        print("Poblacion =  4179 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 24 :
        print("Poblacion =  10032 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 25 :
        print("Poblacion =  145906 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 26 :
        print("Poblacion =  3611 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 27 :
        print("Poblacion =  14592 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 28 :
        print("Poblacion =  14779 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 29 :
        print("Poblacion =  158345 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 30 :
        print("Poblacion =  11019 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 31 :
        print("Poblacion =  58729 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 ==32:
        print("Poblacion =  15205 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  22132 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 9:
    print("Araucanía tiene una poblacion de 1014343 personas en 32 comunas")
    lista_comaraucania  = ["1. Angol","2. Carahue","3. Cholchol","4. Collipulli","5. Cunco", "6. Curacautin",
    "7. Curarrehue","8. Ercilla","9. Freire","10. Galvarino", "11. Gorbea", "12. Lautaro","13. Loncoche","14. Lonquimay",
    "15. Los Sauces", "16.  Lumaco","17. Melipeuco","18. Nueva Imperial", "19. Padre Las Casas", "20. Perquenco","21. Pitrufquen","22. Pucon","23. Puren",
    "24. Renaico","25.   Saavedra", "26.  Temuco","27.  Teodoro Schmidt","28.  Tolten","29. Traiguen","30. Victoria","31.  Vilcun",
    "32. Villarrica"]
    print(lista_comaraucania)
    num9 =input("Escoja un numero de las Comunas de Araucanía:")
    while num9.isnumeric() == False or int(num9) > 32:
        print("Ese no es un numero de alguna comuna de Araucanía")
        num9 = input("Ingrese nuevamente un numero de comuna:")
    num9 = int(num9)
    if num9 == 1:
        print("Poblacion =  56058 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 2:
        print("Poblacion =  25486 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 3:
        print("Poblacion =  12341 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 4:
        print("Poblacion =  26148 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 5:
        print("Poblacion =  18055 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 6:
        print("Poblacion =  18178 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 7:
        print("Poblacion =  7802 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 8:
        print("Poblacion =  8458 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 9 :
        print("Poblacion = 	25446 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 10 :
        print("Poblacion =  12633 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 11 : 
        print("Poblacion =  15148 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 12 :
        print("Poblacion =  40746 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 13 :
        print("Poblacion =  24739 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 14 :
        print("Poblacion =  11049 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 15 :
        print("Poblacion =  7517 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 16 :
        print("Poblacion =  10050 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 17 :
        print("Poblacion =  6265 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 18 :
        print("Poblacion =  33777 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 19 :
        print("Poblacion =  82110 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 20 :
        print("Poblacion =  7223 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 21 :
        print("Poblacion =  26096 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 22 :
        print("Poblacion =  29782 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 23 :
        print("Poblacion =  12188 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 24 :
        print("Poblacion =  10833 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 25 :
        print("Poblacion =  12793 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 26 :
        print("Poblacion =  302931 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 27 :
        print("Poblacion =  15786 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 28 :
        print("Poblacion =  10055 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 29 :
        print("Poblacion =  19314 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 30 :
        print("Poblacion =  35467 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 31 :
        print("Poblacion =  30766 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  59103 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 10:
    print("Los Lagos tiene una poblacion de 891440 personas en 30 comunas")
    lista_comlagos  = ["1. Ancud","2. Calbuco","3. Castro","4. Chaiten","5. Chonchi", "6. Cochamo",
    "7. Curaco de Velez","8. Dalcahue","9. Fresia","10. Frutillar", "11. Futaleufu", "12. Hualaihue","13. Llanquihue","14. Los Muermos",
    "15. Maullin", "16.  Osorno","17.  Palena","18.  Puerto Montt", "19. Puerto Octay", "20. Puerto Varas","21. Puqueldon","22. Purranque","23. Puyehue",
    "24. Queilen","25. Quellon", "26.  Quemchi","27.  Quinchao","28.  Rio Negro ","29. San Juan de la Costa","30. San Pablo"]
    print(lista_comlagos)
    num10 =input("Escoja un numero de las Comunas de Los Lagos:")
    while num10.isnumeric() == False or int(num10) > 30:
        print("Ese no es un numero de alguna comuna de Los Lagos")
        num10 = input("Ingrese nuevamente un numero de comuna:")
    num10 = int(num10)
    if num10 == 1:
        print("Poblacion =  42458 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 2:
        print("Poblacion =  36744 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 3:
        print("Poblacion =  47607 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 4:
        print("Poblacion =  5020 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 5:
        print("Poblacion =  16013 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 6:
        print("Poblacion =  4006 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 7:
        print("Poblacion =  4066 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 8:
        print("Poblacion =  15069 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 9 :
        print("Poblacion = 	12656 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 10 :
        print("Poblacion =  20223 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 11 : 
        print("Poblacion =  2806 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 12 :
        print("Poblacion =  9525 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 13 :
        print("Poblacion =  18621 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 14 :
        print("Poblacion =  17817 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 15 :
        print("Poblacion =  14894 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 16 :
        print("Poblacion =  173410 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 17 :
        print("Poblacion =  1827 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 18 :
        print("Poblacion =  269398 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 19 :
        print("Poblacion =  9192 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 20 :
        print("Poblacion =  48620 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 21 :
        print("Poblacion =  4201 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 22 :
        print("Poblacion =  21080 Personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 23 :
        print("Poblacion =  11787 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 24 :
        print("Poblacion =  5543 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 25 :
        print("Poblacion =  29309 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 26 :
        print("Poblacion =  8783 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 27 :
        print("Poblacion =  8298 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 28 :
        print("Poblacion =  14275 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 29 :
        print("Poblacion =  7639 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  10553 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()


elif regiones == 11:
    print("Aysen tiene una poblacion de 107297 personas en 10 comunas")
    lista_comlagos  = ["1. Aysen","2. Chile Chico","3. Cisnes","4. Cochrane","5. Coyhaique", "6. Guaitecas",
    "7. Lago Verde","8. OHiggins","9. Rio Ibanez","10. Tortel"]
    print(lista_comlagos)
    num11 =input("Escoja un numero de las  Comunas de Aysen:")
    while num11.isnumeric() == False or int(num11) > 10:
        print("Ese no es un numero de alguna comuna de Aysen")
        num11 = input("Ingrese nuevamente un numero de comuna:")
    num11 = int(num11)
    if num11 == 1:
        print("Poblacion =  25002 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 2:
        print("Poblacion =  5121 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 3:
        print("Poblacion =  5828 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 4:
        print("Poblacion =  3685 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 5:
        print("Poblacion =  61210 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 6:
        print("Poblacion =  1599 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 7:
        print("Poblacion =  920 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 8:
        print("Poblacion =  661 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 9 :
        print("Poblacion = 	2699 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	572 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
elif regiones == 12:
    print("Magallanes tiene una poblacion de 178362 personas en 11 comunas")
    lista_commagallanes  = ["1. Antartica","2. Cabo de Hornos","3. 	Laguna Blanca","4. Natales","5. Porvenir", "6. Primavera",
    "7.  Punta Arenas","8. 	Rio Verde","9. San Gregorio","10. Timaukel", "11. Torres del Paine"]
    print(lista_commagallanes)
    num12 =input("Escoja un numero de las Comunas de Magallanes :")
    while num12.isnumeric() == False or int(num12) > 11:
        print("Ese no es un numero de alguna comuna de Magallanes ")
        num12 = input("Ingrese nuevamente un numero de comuna:")
    num12 = int(num12)
    if num12 == 1:
        print("Poblacion =  137 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 2:
        print("Poblacion =  1983 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 3:
        print("Poblacion =  264 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 4:
        print("Poblacion =  23782 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 5:
        print("Poblacion =  7323 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 6:
        print("Poblacion =  694 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 7:
        print("Poblacion =  141984 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 8:
        print("Poblacion =  211 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 9 :
        print("Poblacion = 	681 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 10:
        print("Poblacion =  282 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	1021 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

elif regiones == 14:
    print("Los Rios tiene una poblacion de 405835 personas en 12 comunas")
    lista_comrios  = ["1. Corral","2. Futrono","3. 	La Union","4. Lago Ranco","5. Lanco", "6. Los Lagos",
    "7. Mafil","8. Mariquina","9. Paillaco","10. Panguipulli", "11. Rio Bueno","12. Valdivia"]
    print(lista_comrios)
    num14 =input("Escoja un numero de las Comunas de Los Rios:")
    while num14.isnumeric() == False or int(num14) > 12:
        print("Ese no es un numero de alguna comuna de Los Rios")
        num14 = input("Ingrese nuevamente un numero de comuna:")
    num14 = int(num14)
    if num14 == 1:
        print("Poblacion =  5447 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 2:
        print("Poblacion =  15261 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 3:
        print("Poblacion =  39538 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 4:
        print("Poblacion =  10292 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 5:
        print("Poblacion =  17652 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 6:
        print("Poblacion =  20518 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 7:
        print("Poblacion =  7389 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 8:
        print("Poblacion =  23250 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 9 :
        print("Poblacion = 	20798 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 10:
        print("Poblacion =  35991 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 11:
        print("Poblacion =  32925 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	176774 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()

else:
    print("Arica tiene una poblacion de 252110 personas en 4 comunas")
    lista_comarica  = ["1. Arica ","2. Camarones","3. General Lagos","4. Putre"]
    print(lista_comarica)
    num15 =input("Escoja un numero de las Comunas de Arica:")
    while num15.isnumeric() == False or int(num15) > 4:
        print("Ese no es un numero de alguna comuna de Arica")
        num15 = input("Ingrese nuevamente un numero de comuna:")
    num15 = int(num15)
    if num15 == 1:
        print("Poblacion =  247552 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num15 == 2:
        print("Poblacion =  1233 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num15 == 3:
        print("Poblacion =  810 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  2515 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()  