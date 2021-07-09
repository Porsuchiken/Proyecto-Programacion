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
        ejex=[289,242,250,203,191,167]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 2:
        print("Poblacion = 1375 personas")
        import matplotlib.pyplot as plt
        ejex=[8,9,5,4,1,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 3:
        print("Poblacion = 1583 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,3,3,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 4:
        print("Poblacion = 3000 personas")
        import matplotlib.pyplot as plt
        ejex=[10,7,5,4,0,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 5:
        print("Poblacion = 223463 personas")
        import matplotlib.pyplot as plt
        ejex=[448,402,376,313,271,252]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num == 6:
        print("Poblacion = 5958 personas")    
        import matplotlib.pyplot as plt
        ejex=[25,19,15,17,15,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 17395 personas")
        import matplotlib.pyplot as plt
        ejex=[50,42,31,18,16,10]
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
        ejex=[678,654,570,567,532,510]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 2:
        print("Poblacion = 190336 personas")
        import matplotlib.pyplot as plt
        ejex=[379,360,356,320,317,256]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 3:
        print("Poblacion = 6814 personas")
        import matplotlib.pyplot as plt
        ejex=[25,24,12,10,9,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 4:
        print("Poblacion = 14776 personas")
        import matplotlib.pyplot as plt
        ejex=[28,24,12,8,6,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 5:
        print("Poblacion = 287 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,1,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 6:
        print("Poblacion = 10434 personas")
        import matplotlib.pyplot as plt
        ejex=[28,39,42,28,33,53]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 7:
        print("Poblacion = 1746 personas")
        import matplotlib.pyplot as plt
        ejex=[4,3,1,2,3,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num2 == 8:
        print("Poblacion = 13657 personas")
        import matplotlib.pyplot as plt
        ejex=[13,11,11,22,30,31]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else: 
        print("Poblacion = 28079 personas")
        import matplotlib.pyplot as plt
        ejex=[44,51,40,21,21,25]
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
        ejex=[19,8,4,4,8,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 2:
        print("Poblacion = 19426 personas")
        import matplotlib.pyplot as plt
        ejex=[59,55,57,44,37,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 3:
        print("Poblacion = 13164 personas")
        import matplotlib.pyplot as plt
        ejex=[19,21,33,36,53,47]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 4:
        print("Poblacion = 171766 personas")
        import matplotlib.pyplot as plt
        ejex=[586,549,552,457,523,449]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 5:
        print("Poblacion = 14358 personas")
        import matplotlib.pyplot as plt
        ejex=[34,34,51,47,49,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 6:
        print("Poblacion = 7681 personas")
        import matplotlib.pyplot as plt
        ejex=[15,18,13,7,8,7]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 7:
        print("Poblacion = 11264 personas")
        import matplotlib.pyplot as plt
        ejex=[31,24,19,15,15,15]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num3 == 8:
        print("Poblacion = 14312 personas")
        import matplotlib.pyplot as plt
        ejex=[45,29,16,14,17,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else: 
        print("Poblacion = 57009 personas")
        import matplotlib.pyplot as plt
        ejex=[190,193,137,111,103,106]
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
        ejex=[14,25,33,23,14,15]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 2:
        print("Poblacion =  9546 personas")
        import matplotlib.pyplot as plt
        ejex=[8,5,7,9,8,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 3:
        print("Poblacion =  13884 personas")
        import matplotlib.pyplot as plt
        ejex=[33,28,27,28,22,25]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 4:
        print("Poblacion =  256735 personas")
        import matplotlib.pyplot as plt
        ejex=[520,501,423,362,266,251]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 5:
        print("Poblacion = 32801 personas")
        import matplotlib.pyplot as plt
        ejex=[120,129,133,119,110,79]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 6:
        print("Poblacion =  4450 personas")
        import matplotlib.pyplot as plt
        ejex=[17,10,10,9,12,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 7:
        print("Poblacion = 249656 personas")
        import matplotlib.pyplot as plt
        ejex=[549,540,478,402,333,319]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 8:
        print("Poblacion =  23374 personas")
        import matplotlib.pyplot as plt
        ejex=[46,41,44,43,29,31]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 9 :
        print("Poblacion = 	32527 personas")
        import matplotlib.pyplot as plt
        ejex=[71,79,58,53,52,59]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 10 :
        print("Poblacion =  121269 personas")
        import matplotlib.pyplot as plt
        ejex=[378,372,316,261,163,135]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 11 :
        print("Poblacion =  4675 personas")
        import matplotlib.pyplot as plt
        ejex=[49,37,24,12,6,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 12 :
        print("Poblacion =  12165 personas")
        import matplotlib.pyplot as plt
        ejex=[50,45,34,22,16,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 13 :
        print("Poblacion =  4372 personas")
        import matplotlib.pyplot as plt
        ejex=[5,6,4,6,6,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num4 == 14 :
        print("Poblacion =  29110 personas")
        import matplotlib.pyplot as plt
        ejex=[74,69,60,47,38,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  29741 personas")
        import matplotlib.pyplot as plt
        ejex=[150,125,106,87,80,70]
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
        ejex=[31,31,33,27,23,24]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 2:
        print("Poblacion =  20663 personas")
        import matplotlib.pyplot as plt
        ejex=[52,51,45,45,42,55]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 3:
        print("Poblacion =  53591 personas")
        import matplotlib.pyplot as plt
        ejex=[180,176,163,155,121,74]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 4:
        print("Poblacion =  16482 personas")
        import matplotlib.pyplot as plt
        ejex=[66,69,39,26,18,22]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 5:
        print("Poblacion =  25357 personas")
        import matplotlib.pyplot as plt
        ejex=[127,136,114,73,51,49]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 6:
        print("Poblacion =  29170 personas")
        import matplotlib.pyplot as plt
        ejex=[77,64,39,28,33,36]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 7:
        print("Poblacion =  15213 personas")
        import matplotlib.pyplot as plt
        ejex=[67,54,39,42,58,47]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 8:
        print("Poblacion =  45889 personas")
        import matplotlib.pyplot as plt
        ejex=[80,75,75,54,43,52]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 9 :
        print("Poblacion = 	17742 personas")
        import matplotlib.pyplot as plt
        ejex=[114,91,59,43,29,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 10 :
        print("Poblacion =  14338 personas")
        import matplotlib.pyplot as plt
        ejex=[59,79,70,83,69,48]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 11 : 
        print("Poblacion =  19099 personas")
        import matplotlib.pyplot as plt
        ejex=[31,33,30,18,23,20]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 12 :
        print("Poblacion =  8277 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,1,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 13 :
        print("Poblacion =  1033 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 14 :
        print("Poblacion =  25321 personas")
        import matplotlib.pyplot as plt
        ejex=[73,60,49,49,41,28]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 15 :
        print("Poblacion =  37739 personas")
        import matplotlib.pyplot as plt
        ejex=[134,132,102,92,99,82]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 16 :
        print("Poblacion =  49931 personas")
        import matplotlib.pyplot as plt
        ejex=[118,100,94,74,78,75]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 17 :
        print("Poblacion =  26533 personas")
        import matplotlib.pyplot as plt
        ejex=[103,111,113,108,103,94]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 18 :
        print("Poblacion =  68093 personas")
        import matplotlib.pyplot as plt
        ejex=[294,266,218,153,110,120]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 19 :
        print("Poblacion =  23490 personas")
        import matplotlib.pyplot as plt
        ejex=[71,64,66,70,48,37]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 20 :
        print("Poblacion =  19266 personas")
        import matplotlib.pyplot as plt
        ejex=[57,54,44,36,27,15]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 21 :
        print("Poblacion =  7633 personas")
        import matplotlib.pyplot as plt
        ejex=[22,21,25,22,8,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 22 :
        print("Poblacion =  6201 ersonas")
        import matplotlib.pyplot as plt
        ejex=[3,8,14,21,11,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 23 :
        print("Poblacion =  10558 personas")
        import matplotlib.pyplot as plt
        ejex=[20,27,25,26,33,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 24 :
        print("Poblacion =  20071 personas")
        import matplotlib.pyplot as plt
        ejex=[50,65,69,72,34,27]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 25 :
        print("Poblacion =  17645 personas")
        import matplotlib.pyplot as plt
        ejex=[57,51,38,43,33,42]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 26 :
        print("Poblacion =  97572 personas")
        import matplotlib.pyplot as plt
        ejex=[197,188,202,165,156,125]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 27 :
        print("Poblacion =  167085 personas")
        import matplotlib.pyplot as plt
        ejex=[333,350,331,297,199,167]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 28 :
        print("Poblacion =  36135 personas")
        import matplotlib.pyplot as plt
        ejex=[52,51,52,48,43,33]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 29 :
        print("Poblacion =  11263 personas")
        import matplotlib.pyplot as plt
        ejex=[62,42,37,31,26,21]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 30 :
        print("Poblacion =  96761 personas")
        import matplotlib.pyplot as plt
        ejex=[263,272,259,252,202,175]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 31 :
        print("Poblacion =  20643 personas")
        import matplotlib.pyplot as plt
        ejex=[73,44,67,53,43,52]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 32 :
        print("Poblacion =  83494 personas")
        import matplotlib.pyplot as plt
        ejex=[354,300,253,191,142,129]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 33 :
        print("Poblacion =  16367 personas")
        import matplotlib.pyplot as plt
        ejex=[69,63,60,45,43,37]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 34 :
        print("Poblacion =  11934 personas")
        import matplotlib.pyplot as plt
        ejex=[33,22,19,25,23,20]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 35 :
        print("Poblacion =  315732 personas")
        import matplotlib.pyplot as plt
        ejex=[712,651,589,528,448,468]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 36 :
        print("Poblacion =  139310 personas")
        import matplotlib.pyplot as plt
        ejex=[302,310,274,250,218,192]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num5 == 37 :
        print("Poblacion =  361371 personas")
        import matplotlib.pyplot as plt
        ejex=[620,555,567,521,429,385]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  7994 personas")
        import matplotlib.pyplot as plt
        ejex=[18,18,21,15,15,14]
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
        ejex=[23,17,16,10,8,13]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 2:
        print("Poblacion =  109641 personas")
        import matplotlib.pyplot as plt
        ejex=[521,434,371,312,207,170]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 3:
        print("Poblacion =  28525 personas")
        import matplotlib.pyplot as plt
        ejex=[69,53,57,66,71,63]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 4:
        print("Poblacion =  88956 personas")
        import matplotlib.pyplot as plt
        ejex=[249,236,207,180,119,110]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 5:
        print("Poblacion =  142465 personas")
        import matplotlib.pyplot as plt
        ejex=[533,421,369,286,214,172]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 6:
        print("Poblacion =  180353 personas")
        import matplotlib.pyplot as plt
        ejex=[637,563,491,385,290,285]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 7:
        print("Poblacion =  139195 personas")
        import matplotlib.pyplot as plt
        ejex=[363,282,223,171,164,139]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 8:
        print("Poblacion =  36430 personas")
        import matplotlib.pyplot as plt
        ejex=[156,117,79,64,73,64]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 9 :
        print("Poblacion = 	172000 personas")
        import matplotlib.pyplot as plt
        ejex=[594,518,417,356,293,271]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 10 :
        print("Poblacion =  40014 personas")
        import matplotlib.pyplot as plt
        ejex=[143,109,96,73,58,57]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 11 : 
        print("Poblacion =  206792 personas")
        import matplotlib.pyplot as plt
        ejex=[521,446,407,314,228,187]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 12 :
        print("Poblacion =  112528 personas")
        import matplotlib.pyplot as plt
        ejex=[317,290,236,163,137,130]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 13 :
        print("Poblacion =  142065 personas")
        import matplotlib.pyplot as plt
        ejex=[316,267,238,188,136,118]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 14 :
        print("Poblacion =  40171 personas")
        import matplotlib.pyplot as plt
        ejex=[139,95,87,76,65,54]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 15 :
        print("Poblacion =  100434 personas")
        import matplotlib.pyplot as plt
        ejex=[293,248,190,171,117,98]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 16 :
        print("Poblacion =  402433 personas")
        import matplotlib.pyplot as plt
        ejex=[1163,1026,934,760,614,494]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 17 :
        print("Poblacion =  122557 personas")
        import matplotlib.pyplot as plt
        ejex=[413,352,259,230,193,152]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 18 :
        print("Poblacion =  189335 personas")
        import matplotlib.pyplot as plt
        ejex=[604,504,487,362,266,203]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 19 :
        print("Poblacion =  100252 personas")
        import matplotlib.pyplot as plt
        ejex=[258,209,178,152,124,108]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 20 :
        print("Poblacion =  126898 personas")
        import matplotlib.pyplot as plt
        ejex=[365,307,250,185,129,101]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 21 :
        print("Poblacion =  330759 personas")
        import matplotlib.pyplot as plt
        ejex=[564,480,414,325,282,234]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 22 :
        print("Poblacion =  124076 Personas")
        import matplotlib.pyplot as plt
        ejex=[323,265,236,177,153,131]
        ejey=[18,21,25,28,2,5]
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.plot(ejex,ejey)
        plt.show()
    elif num13 == 23 :
        print("Poblacion =  103865 personas")
        import matplotlib.pyplot as plt
        ejex=[265,229,178,154,121,109]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 24 :
        print("Poblacion =  104403 personas")
        import matplotlib.pyplot as plt
        ejex=[433,423,357,280,223,191]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 25 :
        print("Poblacion =  134635 personas")
        import matplotlib.pyplot as plt
        ejex=[363,344,302,228,179,161]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 26 :
        print("Poblacion =  578605 personas")
        import matplotlib.pyplot as plt
        ejex=[1481,1262,1062,864,681,605]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 27 :
        print("Poblacion =  14926 personas")
        import matplotlib.pyplot as plt
        ejex=[63,52,40,35,43,32]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 28 :
        print("Poblacion =  141612 personas")
        import matplotlib.pyplot as plt
        ejex=[378,313,256,213,172,182]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 29 :
        print("Poblacion =  250192 personas")
        import matplotlib.pyplot as plt
        ejex=[444,398,324,246,220,196]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 30 :
        print("Poblacion =  74188 personas")
        import matplotlib.pyplot as plt
        ejex=[337,284,221,187,125,113]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 31 :
        print("Poblacion =  82766 personas")
        import matplotlib.pyplot as plt
        ejex=[279,239,207,196,151,122]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 32 :
        print("Poblacion =  107803 personas")
        import matplotlib.pyplot as plt
        ejex=[431,326,303,263,225,188]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 33 :
        print("Poblacion =  101058 personas")
        import matplotlib.pyplot as plt
        ejex=[334,313,255,221,179,154]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 34 :
        print("Poblacion =  266798 personas")
        import matplotlib.pyplot as plt
        ejex=[914,861,795,691,589,531]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 35 :
        print("Poblacion =  30433 personas")
        import matplotlib.pyplot as plt
        ejex=[116,84,72,67,47,44]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 36 :
        print("Poblacion =  157749 personas")
        import matplotlib.pyplot as plt
        ejex=[284,244,188,141,115,91]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 37 :
        print("Poblacion =  253139 personas")
        import matplotlib.pyplot as plt
        ejex=[737,629,525,434,352,297]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 38 :
        print("Poblacion =  645909 personas")
        import matplotlib.pyplot as plt
        ejex=[1909,1776,1550,1346,1000,808]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 39 :
        print("Poblacion =  254694 personas") 
        import matplotlib.pyplot as plt
        ejex=[570,518,395,321,263,230]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 40 :
        print("Poblacion =  136368 personas")
        import matplotlib.pyplot as plt
        ejex=[529,465,364,290,219,189]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 41 :
        print("Poblacion =  190075 personas")
        import matplotlib.pyplot as plt
        ejex=[420,356,307,251,224,189]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 42 :
        print("Poblacion =  160847 personas")
        import matplotlib.pyplot as plt
        ejex=[836,720,614,464,380,318]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 43 :
        print("Poblacion =  334836 personas")
        import matplotlib.pyplot as plt
        ejex=[1021,856,718,570,439,402]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 44 :
        print("Poblacion =  103485 personas")
        import matplotlib.pyplot as plt
        ejex=[396,342,304,250,166,148]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 45 :
        print("Poblacion =  18644 personas")
        import matplotlib.pyplot as plt
        ejex=[71,52,37,36,27,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 46 :
        print("Poblacion =  133059 personas")
        import matplotlib.pyplot as plt
        ejex=[403,333,282,236,190,192]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 47 :
        print("Poblacion =  11953 personas")
        import matplotlib.pyplot as plt
        ejex=[23,17,16,12,15,18]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 48 :
        print("Poblacion =  86510 personas")
        import matplotlib.pyplot as plt
        ejex=[215,171,133,118,91,84]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 49 :
        print("Poblacion =  503147 personas")
        import matplotlib.pyplot as plt
        ejex=[1254,1035,717,563,428,393]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 50 :
        print("Poblacion =  81838 personas")
        import matplotlib.pyplot as plt
        ejex=[156,150,121,100,73,85]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num13 == 51 :
        print("Poblacion =  21477 personas")
        import matplotlib.pyplot as plt
        ejex=[76,53,41,25,18,17]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  96774 personas")
        import matplotlib.pyplot as plt
        ejex=[124,107,99,81,74,55]
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
        ejex=[47,49,46,24,18,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 2:
        print("Poblacion =  37696 personas")
        import matplotlib.pyplot as plt
        ejex=[66,72,81,	67,	35,	32,]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 3:
        print("Poblacion =  14096 personas")
        import matplotlib.pyplot as plt
        ejex=[41,41,25,15,10,17]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 4:
        print("Poblacion =  7831 personas")
        import matplotlib.pyplot as plt
        ejex=[13,17,14,7,1,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 5:
        print("Poblacion =  21263 personas")
        import matplotlib.pyplot as plt
        ejex=[29,15,12,18,15,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 6:
        print("Poblacion =  22700 personas")
        import matplotlib.pyplot as plt
        ejex=[42,42,37,28,16,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 7:
        print("Poblacion =  36504 personas")
        import matplotlib.pyplot as plt
        ejex=[139,124,95,78,61,44]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 8:
        print("Poblacion =  3114 personas")
        import matplotlib.pyplot as plt
        ejex=[3,6,7,8,11,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 9 :
        print("Poblacion = 	26749 personas")
        import matplotlib.pyplot as plt
        ejex=[53,54,52,60,56,55]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 10 :
        print("Poblacion =  6765 personas")
        import matplotlib.pyplot as plt
        ejex=[35,25,14,20,15,5.]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 11 : 
        print("Poblacion =  7289 personas")
        import matplotlib.pyplot as plt
        ejex=[7,10,7,7,6,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 12 :
        print("Poblacion =  59913 personas")
        import matplotlib.pyplot as plt
        ejex=[138,139,108,74,72,66]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 13 :
        print("Poblacion =  14163 personas")
        import matplotlib.pyplot as plt
        ejex=[37,23,22,20,18,13]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 14 :
        print("Poblacion =  7632 personas")
        import matplotlib.pyplot as plt
        ejex=[16,12,5,4,3,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 15 :
        print("Poblacion =  27462 personas")
        import matplotlib.pyplot as plt
        ejex=[137,108,94,82,73,50]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 16 :
        print("Poblacion =  19141 personas")
        import matplotlib.pyplot as plt
        ejex=[30,29,17,17,29,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 17 :
        print("Poblacion =  6904 personas")
        import matplotlib.pyplot as plt
        ejex=[47,39,24,18,7,10]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 18 :
        print("Poblacion =  14624 personas")
        import matplotlib.pyplot as plt
        ejex=[36,25,17,18,6,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 19 :
        print("Poblacion =  13299 personas")
        import matplotlib.pyplot as plt
        ejex=[13,26,17,16,6,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 20 :
        print("Poblacion =  6349 personas")
        import matplotlib.pyplot as plt
        ejex=[17,12,12,7,4,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 21 :
        print("Poblacion =  11848 personas")
        import matplotlib.pyplot as plt
        ejex=[18,14,13,11,7,13]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 22 :
        print("Poblacion =  14952 Personas")
        import matplotlib.pyplot as plt
        ejex=[42,38,38,28,18,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 23 :
        print("Poblacion =  20743 personas")
        import matplotlib.pyplot as plt
        ejex=[69,57,47,30,18,11,]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 24 :
        print("Poblacion =  17882 personas")
        import matplotlib.pyplot as plt
        ejex=[33,37,32,50,43,16]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 25 :
        print("Poblacion =  9164 personas")
        import matplotlib.pyplot as plt
        ejex=[29,25,28,23,19,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 26 :
        print("Poblacion =  3531 personas")
        import matplotlib.pyplot as plt
        ejex=[10,14,10,3,0,	0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 27 :
        print("Poblacion =  13877 personas")
        import matplotlib.pyplot as plt
        ejex=[26,29,27,25,20,19]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 28 :
        print("Poblacion =  265211 personas")
        import matplotlib.pyplot as plt
        ejex=[795,699,546,420,347,308]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 29 :
        print("Poblacion =  63710 personas")
        import matplotlib.pyplot as plt
        ejex=[202,158,124,91,79,83]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 30 :
        print("Poblacion =  30371 personas")
        import matplotlib.pyplot as plt
        ejex=[60,59,42,35,36,46]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 == 31 :
        print("Poblacion =  78642 personas")
        import matplotlib.pyplot as plt
        ejex=[147,146,121,91,73,55]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num6 ==32:
        print("Poblacion =  50617 personas")
        import matplotlib.pyplot as plt
        ejex=[118,94,99,87,69,70]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  41096 personas")
        import matplotlib.pyplot as plt
        ejex=[95,92,63,44,44,43]
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
        ejex=[88,98,103,119,109,93]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 2:
        print("Poblacion =  9331 personas")
        import matplotlib.pyplot as plt
        ejex=[23,30,26,18,15,10]
        ejey=[18,21,25,28,2,5]
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.plot(ejex,ejey)
        plt.show()
    elif num7 == 3:
        print("Poblacion =  22565 personas")
        import matplotlib.pyplot as plt
        ejex=[128,110,83,78,73,56]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 4:
        print("Poblacion =  50348 personas")
        import matplotlib.pyplot as plt
        ejex=[135,127,141,142,150,144]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 5:
        print("Poblacion =  9426 personas")
        import matplotlib.pyplot as plt
        ejex=[26,22,22,21,12,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 6:
        print("Poblacion =  163626 personas")
        import matplotlib.pyplot as plt
        ejex=[402,357,277,277,205,153]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 7:
        print("Poblacion =  4206 personas")
        import matplotlib.pyplot as plt
        ejex=[8,11,6,5,7,8]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 8:
        print("Poblacion =  10222 personas")
        import matplotlib.pyplot as plt
        ejex=[17,14,16,17,16,17]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 9 :
        print("Poblacion = 	6989 personas")
        import matplotlib.pyplot as plt
        ejex=[7,4,9,12,15,15]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 10 :
        print("Poblacion =  101073 personas")
        import matplotlib.pyplot as plt
        ejex=[307,267,258,240,203,183]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 11 : 
        print("Poblacion =  32810 personas")
        import matplotlib.pyplot as plt
        ejex=[178,138,100,70,39,35]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 12 :
        print("Poblacion =  60000 personas")
        import matplotlib.pyplot as plt
        ejex=[144,137,117,114,84,79]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 13 :
        print("Poblacion =  49800 personas")
        import matplotlib.pyplot as plt
        ejex=[112,121,111,98,103,69]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 14 :
        print("Poblacion =  44544 personas")
        import matplotlib.pyplot as plt
        ejex=[238,195,147,155,139117]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 15 :
        print("Poblacion =  9083 personas")
        import matplotlib.pyplot as plt
        ejex=[35,30,18,12,6,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 16 :
        print("Poblacion =  8092 personas")
        import matplotlib.pyplot as plt
        ejex=[44,40,32,40,31,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 17 :
        print("Poblacion =  8601 personas")
        import matplotlib.pyplot as plt
        ejex=[29,32,18,16,6,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 18 :
        print("Poblacion =  11248 personas")
        import matplotlib.pyplot as plt
        ejex=[22,24,23,20,15,14]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 19 :
        print("Poblacion =  21071 personas")
        import matplotlib.pyplot as plt
        ejex=[48,68,75,73,67,69]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 20 :
        print("Poblacion =  14753 personas")
        import matplotlib.pyplot as plt
        ejex=[19,18,10,8,26,42]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 21 :
        print("Poblacion =  16170 personas")
        import matplotlib.pyplot as plt
        ejex=[60,52,26,19,26,22]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 22 :
        print("Poblacion =  19469 Personas")
        import matplotlib.pyplot as plt
        ejex=[48,41,33,40,20,14]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 23 :
        print("Poblacion =  46292 personas")
        import matplotlib.pyplot as plt
        ejex=[186,188,165,114,105,81]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 24 :
        print("Poblacion =  49451 personas")
        import matplotlib.pyplot as plt
        ejex=[120,96,84,81,55,41]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 25 :
        print("Poblacion =  9959 personas")
        import matplotlib.pyplot as plt
        ejex=[54,47,50,37,39,31]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 26 :
        print("Poblacion =  236724 personas")
        import matplotlib.pyplot as plt
        ejex=[649,586,484,435,403,392]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 27 :
        print("Poblacion =  30850  personas")
        import matplotlib.pyplot as plt
        ejex=[122,113,81,82,49,33]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 28 :
        print("Poblacion =  4381 personas")
        import matplotlib.pyplot as plt
        ejex=[7,6,1,3,4,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num7 == 29 :
        print("Poblacion =  17512  personas")
        import matplotlib.pyplot as plt
        ejex=[49,37,44,27,39,37]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  19200 personas")
        import matplotlib.pyplot as plt
        ejex=[67,71,60,64,43,30]
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
        ejex=[39,28,41,34,28,25]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 2:
        print("Poblacion = 198624 personas")
        import matplotlib.pyplot as plt
        ejex=[369,347,330,288,266,227]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 3:
        print("Poblacion = 33827 personas")
        import matplotlib.pyplot as plt
        ejex=[54,42,39,46,36,33]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 4:
        print("Poblacion = 5275 personas")
        import matplotlib.pyplot as plt
        ejex=[6,11,10,5,4,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 5:
        print("Poblacion = 	16845 personas")
        import matplotlib.pyplot as plt
        ejex=[29,22,19,13,4,10]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 6:
        print("Poblacion =  28375 personas")
        import matplotlib.pyplot as plt
        ejex=[79,85,44,44,44,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 7:
        print("Poblacion =  12334 personas")
        import matplotlib.pyplot as plt
        ejex=[16,21,19,18,5,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 8:
        print("Poblacion =  5414 personas")
        import matplotlib.pyplot as plt
        ejex=[27,17,5,6,9,10]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 9 :
        print("Poblacion = 	11567 personas")
        import matplotlib.pyplot as plt
        ejex=[18,24,28,22,8,14]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 10 :
        print("Poblacion =  8639 personas")
        import matplotlib.pyplot as plt
        ejex=[30,29,27,28,30,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 11 : 
        print("Poblacion =  11880 personas")
        import matplotlib.pyplot as plt
        ejex=[22,18,19,19,21,15]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 12 :
        print("Poblacion =  4940 personas")
        import matplotlib.pyplot as plt
        ejex=[20,17,13,11,14,12]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 13 :
        print("Poblacion =  18777 personas")
        import matplotlib.pyplot as plt
        ejex=[49,43,29,28,24,37]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 14 :
        print("Poblacion =  12192 personas")
        import matplotlib.pyplot as plt
        ejex=[21,17,15,18,23,17]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 15 :
        print("Poblacion =  6261 personas")
        import matplotlib.pyplot as plt
        ejex=[20,8,3,7,5,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 16 :
        print("Poblacion =  56252 personas")
        import matplotlib.pyplot as plt
        ejex=[258,256,158,132,116,84]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 17 :
        print("Poblacion =  4654 personas")
        import matplotlib.pyplot as plt
        ejex=[19,11,8,6,1,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 18 :
        print("Poblacion =  16624 personas")
        import matplotlib.pyplot as plt
        ejex=[32,23,24,25,19,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 19 :
        print("Poblacion =  12172 personas")
        import matplotlib.pyplot as plt
        ejex=[21,33,32,20,5,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num16 == 20 :
        print("Poblacion =  5696 personas")
        import matplotlib.pyplot as plt
        ejex=[12,10,6,3,5,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  18596 personas")
        import matplotlib.pyplot as plt
        ejex=[36,37,33,24,14,12]
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
        ejex=[24,25,17,23,18,24]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 2:
        print("Poblacion =  4306 personas")
        import matplotlib.pyplot as plt
        ejex=[12,12,6,10,9,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 3:
        print("Poblacion =  38679 personas")
        import matplotlib.pyplot as plt
        ejex=[87,96,100,86,71,73]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 4:
        print("Poblacion =  30725 personas")
        import matplotlib.pyplot as plt
        ejex=[72,72,52,39,29,20]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 5:
        print("Poblacion =  37003 personas")
        import matplotlib.pyplot as plt
        ejex=[113,85,72,77,62,51]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 6:
        print("Poblacion =  91180 personas")
        import matplotlib.pyplot as plt
        ejex=[235,214,167,140,107,91]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 7:
        print("Poblacion =  238092 personas")
        import matplotlib.pyplot as plt
        ejex=[510,481,423,368,323,311]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 8:
        print("Poblacion =  6330 personas")
        import matplotlib.pyplot as plt
        ejex=[6,6,3,1,7,20]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 9 :
        print("Poblacion = 	125829 personas")
        import matplotlib.pyplot as plt
        ejex=[227,227,264,262,246,222]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 10 :
        print("Poblacion =  33892 personas")
        import matplotlib.pyplot as plt
        ejex=[95,109,96,89,58,40]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 11 : 
        print("Poblacion =  11841 personas")
        import matplotlib.pyplot as plt
        ejex=[23,32,43,41,35,21]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 12 :
        print("Poblacion =  97273 personas")
        import matplotlib.pyplot as plt
        ejex=[231,224,214,178,140,131]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 13 :
        print("Poblacion =  26201 personas")
        import matplotlib.pyplot as plt
        ejex=[53,52,43,31,31,21]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 14 :
        print("Poblacion =  23873 personas")
        import matplotlib.pyplot as plt
        ejex=[96,82,66,50,45,44]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 15 :
        print("Poblacion =  27100 personas")
        import matplotlib.pyplot as plt
        ejex=[118,102,106,101,97,83]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 16 :
        print("Poblacion =  22524 personas")
        import matplotlib.pyplot as plt
        ejex=[72,64,56,52,63,64]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 17 :
        print("Poblacion =  218515 personas")
        import matplotlib.pyplot as plt
        ejex=[761,599,491,412,348,265]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 18 :
        print("Poblacion =  45750 personas")
        import matplotlib.pyplot as plt
        ejex=[112,86,88,73,50,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 19 :
        print("Poblacion =  31041 personas")
        import matplotlib.pyplot as plt
        ejex=[84,80,80,76,70,61]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 20 :
        print("Poblacion =  27944 personas")
        import matplotlib.pyplot as plt
        ejex=[100,100,86,83,75,54]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 21 :
        print("Poblacion =  10429 personas")
        import matplotlib.pyplot as plt
        ejex=[26,16,14,21,26,27]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 22 :
        print("Poblacion =  49865 Personas")
        import matplotlib.pyplot as plt
        ejex=[84,84,80,70,60,71]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 23 :
        print("Poblacion =  4179 personas")
        import matplotlib.pyplot as plt
        ejex=[7,7,1,1,3,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 24 :
        print("Poblacion =  10032 personas")
        import matplotlib.pyplot as plt
        ejex=[16,17,10,11,13,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 25 :
        print("Poblacion =  145906 personas")
        import matplotlib.pyplot as plt
        ejex=[320,236,230,272,262,188]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 26 :
        print("Poblacion =  3611 personas")
        import matplotlib.pyplot as plt
        ejex=[2,4,4,5,8,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 27 :
        print("Poblacion =  14592 personas")
        import matplotlib.pyplot as plt
        ejex=[41,18,17,12,6,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 28 :
        print("Poblacion =  14779 personas")
        import matplotlib.pyplot as plt
        ejex=[58,66,80,96,92,77]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 29 :
        print("Poblacion =  158345 personas")
        import matplotlib.pyplot as plt
        ejex=[330,334,271,224,204,191]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 30 :
        print("Poblacion =  11019 personas")
        import matplotlib.pyplot as plt
        ejex=[35,29,45,43,33,22]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 == 31 :
        print("Poblacion =  58729 personas")
        import matplotlib.pyplot as plt
        ejex=[117,106,82,93,92,90]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num8 ==32:
        print("Poblacion =  15205 personas")
        import matplotlib.pyplot as plt
        ejex=[22,25,39,28,21,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  22132 personas")
        import matplotlib.pyplot as plt
        ejex=[76,80,77,43,42,40]
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
        ejex=[71,62,60,91,79,65]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 2:
        print("Poblacion =  25486 personas")
        import matplotlib.pyplot as plt
        ejex=[61,70,77,59,40,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 3:
        print("Poblacion =  12341 personas")
        import matplotlib.pyplot as plt
        ejex=[24,28,22,19,20,18]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 4:
        print("Poblacion =  26148 personas")
        import matplotlib.pyplot as plt
        ejex=[115,101,102,96,84,65]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 5:
        print("Poblacion =  18055 personas")
        import matplotlib.pyplot as plt
        ejex=[53,59,69,49,16,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 6:
        print("Poblacion =  18178 personas")
        import matplotlib.pyplot as plt
        ejex=[55,41,35,46,43,35]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 7:
        print("Poblacion =  7802 personas")
        import matplotlib.pyplot as plt
        ejex=[43,42,34,32,29,31]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 8:
        print("Poblacion =  8458 personas")
        import matplotlib.pyplot as plt
        ejex=[28,37,31,30,24,19]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 9 :
        print("Poblacion = 	25446 personas")
        import matplotlib.pyplot as plt
        ejex=[92,82,62,69,52,27]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 10 :
        print("Poblacion =  12633 personas")
        import matplotlib.pyplot as plt
        ejex=[63,62,47,52,61,63]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 11 : 
        print("Poblacion =  15148 personas")
        import matplotlib.pyplot as plt
        ejex=[55,42,39,38,23,29]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 12 :
        print("Poblacion =  40746 personas")
        import matplotlib.pyplot as plt
        ejex=[95,76,84,102,101,101]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 13 :
        print("Poblacion =  24739 personas")
        import matplotlib.pyplot as plt
        ejex=[56,63,82,58,49,31]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 14 :
        print("Poblacion =  11049 personas")
        import matplotlib.pyplot as plt
        ejex=[48,54,47,60,44,40]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 15 :
        print("Poblacion =  7517 personas")
        import matplotlib.pyplot as plt
        ejex=[42,50,50,39,36,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 16 :
        print("Poblacion =  10050 personas")
        import matplotlib.pyplot as plt
        ejex=[191,152,103,93,102,93]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 17 :
        print("Poblacion =  6265 personas")
        import matplotlib.pyplot as plt
        ejex=[17,11,7,7,6,11]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 18 :
        print("Poblacion =  33777 personas")
        import matplotlib.pyplot as plt
        ejex=[15,19,12,12,7,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 19 :
        print("Poblacion =  82110 personas")
        import matplotlib.pyplot as plt
        ejex=[8,7,7,7,3,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 20 :
        print("Poblacion =  7223 personas")
        import matplotlib.pyplot as plt
        ejex=[41,47,44,35,46,42]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 21 :
        print("Poblacion =  26096 personas")
        import matplotlib.pyplot as plt
        ejex=[178,200,182,147,113,98]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 22 :
        print("Poblacion =  29782 Personas")
        import matplotlib.pyplot as plt
        ejex=[9,8,19,14,13,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 23 :
        print("Poblacion =  12188 personas")
        import matplotlib.pyplot as plt
        ejex=[86,85,74,60,54,47]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 24 :
        print("Poblacion =  10833 personas")
        import matplotlib.pyplot as plt
        ejex=[191,152,103,93,102,93]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 25 :
        print("Poblacion =  12793 personas")
        import matplotlib.pyplot as plt
        ejex=[8,7,7,7,3,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 26 :
        print("Poblacion =  302931 personas")
        import matplotlib.pyplot as plt
        ejex=[16,28,34,30,35,26]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 27 :
        print("Poblacion =  15786 personas")
        import matplotlib.pyplot as plt
        ejex=[48,51,46,38,32,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 28 :
        print("Poblacion =  10055 personas")
        import matplotlib.pyplot as plt
        ejex=[504,465,456,455,390,344]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 29 :
        print("Poblacion =  19314 personas")
        import matplotlib.pyplot as plt
        ejex=[]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 30 :
        print("Poblacion =  35467 personas")
        import matplotlib.pyplot as plt
        ejex=[51,55,84,69,83,45]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num9 == 31 :
        print("Poblacion =  30766 personas")
        import matplotlib.pyplot as plt
        ejex=[32,47,46,36,30,29]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  59103 personas")
        import matplotlib.pyplot as plt
        ejex=[43,41,38,37,38,33]
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
        ejex=[104,86,58,64,44,34]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 2:
        print("Poblacion =  36744 personas")
        import matplotlib.pyplot as plt
        ejex=[105,99,55,26,12,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 3:
        print("Poblacion =  47607 personas")
        import matplotlib.pyplot as plt
        ejex=[138,123,103,117,100,77]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 4:
        print("Poblacion =  5020 personas")
        import matplotlib.pyplot as plt
        ejex=[28,21,13,7,9,	6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 5:
        print("Poblacion =  16013 personas")
        import matplotlib.pyplot as plt
        ejex=[49,34,24,16,23,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 6:
        print("Poblacion =  4006 personas")
        import matplotlib.pyplot as plt
        ejex=[7,2,1,2,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 7:
        print("Poblacion =  4066 personas")
        import matplotlib.pyplot as plt
        ejex=[26,14,14,6,2,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 8:
        print("Poblacion =  15069 personas")
        import matplotlib.pyplot as plt
        ejex=[41,38,35,43,35,29]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 9 :
        print("Poblacion = 	12656 personas")
        import matplotlib.pyplot as plt
        ejex=[14,12,15,22,20,19]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 10 :
        print("Poblacion =  20223 personas")
        import matplotlib.pyplot as plt
        ejex=[44,45,47,43,34,32]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 11 : 
        print("Poblacion =  2806 personas")
        import matplotlib.pyplot as plt
        ejex=[1,1,1,2,1,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 12 :
        print("Poblacion =  9525 personas")
        import matplotlib.pyplot as plt
        ejex=[8,5,4,2,1,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 13 :
        print("Poblacion =  18621 personas")
        import matplotlib.pyplot as plt
        ejex=[43,36,40,37,21,28]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 14 :
        print("Poblacion =  17817 personas")
        import matplotlib.pyplot as plt
        ejex=[18,16,21,25,20,23]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 15 :
        print("Poblacion =  14894 personas")
        import matplotlib.pyplot as plt
        ejex=[21,18,6,14,16,16,]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 16 :
        print("Poblacion =  173410 personas")
        import matplotlib.pyplot as plt
        ejex=[380,318,280,314,314,299]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 17 :
        print("Poblacion =  1827 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,1,2,1,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 18 :
        print("Poblacion =  269398 personas")
        import matplotlib.pyplot as plt
        ejex=[545,447,384,383,358,295,]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 19 :
        print("Poblacion =  9192 personas")
        import matplotlib.pyplot as plt
        ejex=[13,17,25,18,8,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 20 :
        print("Poblacion =  48620 personas")
        import matplotlib.pyplot as plt
        ejex=[121,127,109,108,79,60]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 21 :
        print("Poblacion =  4201 personas")
        import matplotlib.pyplot as plt
        ejex=[17,10,19,29,39,36]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 22 :
        print("Poblacion =  21080 Personas")
        import matplotlib.pyplot as plt
        ejex=[50,51,41,25,28,30]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 23 :
        print("Poblacion =  11787 personas")
        import matplotlib.pyplot as plt
        ejex=[33,31,35,37,34,37]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 24 :
        print("Poblacion =  5543 personas")
        import matplotlib.pyplot as plt
        ejex=[23,20,18,17,10,10]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 25 :
        print("Poblacion =  29309 personas")
        import matplotlib.pyplot as plt
        ejex=[43,53,45,18,20,33]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 26 :
        print("Poblacion =  8783 personas")
        import matplotlib.pyplot as plt
        ejex=[17,12,14,8,5,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 27 :
        print("Poblacion =  8298 personas")
        import matplotlib.pyplot as plt
        ejex=[11,10,5,6,5,6]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 28 :
        print("Poblacion =  14275 personas")
        import matplotlib.pyplot as plt
        ejex=[73,71,59,80,73,75]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num10 == 29 :
        print("Poblacion =  7639 personas")
        import matplotlib.pyplot as plt
        ejex=[19,17,19,18,23,16]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  10553 personas")
        import matplotlib.pyplot as plt
        ejex=[20,20,27,30,29,27]
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
        ejex=[198,147,111,81,75,65]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 2:
        print("Poblacion =  5121 personas")
        import matplotlib.pyplot as plt
        ejex=[35,16,9,9,8,7]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 3:
        print("Poblacion =  5828 personas")
        import matplotlib.pyplot as plt
        ejex=[41,34,18,19,16,21]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 4:
        print("Poblacion =  3685 personas")
        import matplotlib.pyplot as plt
        ejex=[22,22,19,15,10,5]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 5:
        print("Poblacion =  61210 personas")
        import matplotlib.pyplot as plt
        ejex=[227,234,192,156,127,127]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 6:
        print("Poblacion =  1599 personas")
        import matplotlib.pyplot as plt
        ejex=[1,1,2,0,1,4]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 7:
        print("Poblacion =  920 personas")
        import matplotlib.pyplot as plt
        ejex=[4,3,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 8:
        print("Poblacion =  661 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num11 == 9 :
        print("Poblacion = 	2699 personas")
        import matplotlib.pyplot as plt
        ejex=[26,29,14,13,7,1]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	572 personas")
        import matplotlib.pyplot as plt
        ejex=[1,2,7,6,1,0]
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
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 2:
        print("Poblacion =  1983 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 3:
        print("Poblacion =  264 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 4:
        print("Poblacion =  23782 personas")
        import matplotlib.pyplot as plt
        ejex=[60,45,46,38,25,24]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 5:
        print("Poblacion =  7323 personas")
        import matplotlib.pyplot as plt
        ejex=[24,26,24,25,23,19]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 6:
        print("Poblacion =  694 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 7:
        print("Poblacion =  141984 personas")
        import matplotlib.pyplot as plt
        ejex=[201,160,139,110,118,109]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 8:
        print("Poblacion =  211 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,2,3]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 9 :
        print("Poblacion = 	681 personas")
        import matplotlib.pyplot as plt
        ejex=[1,0,0,0,0,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num12 == 10:
        print("Poblacion =  282 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	1021 personas")
        import matplotlib.pyplot as plt
        ejex=[0,0,0,0,0,0]
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
        ejex=[21,11,13,11,9,10]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 2:
        print("Poblacion =  15261 personas")
        import matplotlib.pyplot as plt
        ejex=[149,118,97,118,136,151]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 3:
        print("Poblacion =  39538 personas")
        import matplotlib.pyplot as plt
        ejex=[108,104,96,107,85,73.]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 4:
        print("Poblacion =  10292 personas")
        import matplotlib.pyplot as plt
        ejex=[122,108,111,93,98,87]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 5:
        print("Poblacion =  17652 personas")
        import matplotlib.pyplot as plt
        ejex=[118,99,81,67,69,67]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 6:
        print("Poblacion =  20518 personas")
        import matplotlib.pyplot as plt
        ejex=[189,164,134,129,109,87]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 7:
        print("Poblacion =  7389 personas")
        import matplotlib.pyplot as plt
        ejex=[29,29,43,44,31,24]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 8:
        print("Poblacion =  23250 personas")
        import matplotlib.pyplot as plt
        ejex=[60,47,54,42,49,40]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 9 :
        print("Poblacion = 	20798 personas")
        import matplotlib.pyplot as plt
        ejex=[134,112,107,77,83,75]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 10:
        print("Poblacion =  35991 personas")
        import matplotlib.pyplot as plt
        ejex=[295,268,270,241,259,272]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num14 == 11:
        print("Poblacion =  32925 personas")
        import matplotlib.pyplot as plt
        ejex=[90,69,69,74,81,84]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion = 	176774 personas")
        import matplotlib.pyplot as plt
        ejex=[561,490,487,438,364,307,]
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
        ejex=[766,781,816,730,624,581]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num15 == 2:
        print("Poblacion =  1233 personas")
        import matplotlib.pyplot as plt
        ejex=[0,1,1,2,5,7]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    elif num15 == 3:
        print("Poblacion =  810 personas")
        import matplotlib.pyplot as plt
        ejex=[10,11,5,2,3,2]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()
    else:
        print("Poblacion =  2515 personas")
        import matplotlib.pyplot as plt
        ejex=[16,12,11,8,12,9]
        ejey=[18,21,25,28,2,5]
        plt.plot(ejex,ejey)
        plt.xlabel('Junio y Julio 2020')
        plt.ylabel('Contagiados del Dia')
        plt.show()  