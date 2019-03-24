from lxml import etree
doc = etree.parse('radares.xml')

from funcionesxml import provincias
from funcionesxml import radares
from funcionesxml import poblacion
from funcionesxml import carreteras
from funcionesxml import localizar


while (True):
    print('''
    Elige una opcion:
    1.Mostrar el nombre de las provincias de las que tenemos información sobre radares.
    2.Mostrar la cantidad de radares de los que tenemos información.
    3.Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
    4.Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
    5.Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).
    0-Salir''')
    opcion=int(input("Opcion: "))

    if opcion==1:
    #Mostrar el nombre de las provincias de las que tenemos información sobre radares.


        for i in provincias(doc):
            print ("______________")
            print (i)


    elif opcion==2:

    #Mostrar la cantidad de radares de los que tenemos información.
         print ("Hay un total de ",int(radares(doc)),"radares")

    elif opcion==3:

    #Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
        provincia=input("Dime una provincia:").capitalize()

        print ("Carreteras de la provincia de",provincia)
        print ("..........................................")
        for carreteras in poblacion(provincia,doc)[0]:
            print (carreteras)
        print ("")
        print ("Tiene un total de",poblacion(provincia,doc)[1],"radares")

    elif opcion==4:
    #Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
        carretera=input("Dime una carretera:")

        print ("Provincia/s de la carretera",carretera)
        print ("..........................................")
        for información in carreteras(carretera,doc)[0]:
            print ("-",información)
        print ("")
        print ("Radares de la carretera",carretera)
        print ("..........................................")
        for radaresinicio,radaresfinal in zip(carreteras(carretera,doc)[1],carreteras(carretera,doc)[2]):
            print (radaresinicio,"-",radaresfinal)
    elif opcion==5:
    #Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).

        carretera=input("Dime una carretera:")
        print ("La carretera de",carretera,"tiene",localizar(carretera,doc)[0],"radares")

        cantidad = 1
        for latitud,longitud in zip(localizar(carretera,doc)[1],localizar(carretera,doc)[2]):
            print(cantidad,"-","http://www.openstreetmap.org/#map=20/%s/%s"%(latitud,longitud))
            cantidad = cantidad + 1
            
    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
