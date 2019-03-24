from lxml import etree
doc = etree.parse('radares.xml')

from funciones import provincias

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

    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
