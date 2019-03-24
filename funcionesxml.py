    #Mostrar el nombre de las provincias de las que tenemos información sobre radares.

def provincias(doc):
    lista = doc.xpath("//PROVINCIA/NOMBRE/text()")
    return lista

    #Mostrar la cantidad de radares de los que tenemos información.

def radares(doc):
    lista = doc.xpath("count(//RADAR)")
    return lista

    #Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.

def poblacion(provincia,doc):
    carretera = doc.xpath('//PROVINCIA[NOMBRE="%s"]/./CARRETERA/DENOMINACION/text()'%provincia)
    radares = int(doc.xpath('count(//PROVINCIA[NOMBRE="%s"]/./CARRETERA/RADAR)'%provincia))
    info = [carretera,radares]
    return info
