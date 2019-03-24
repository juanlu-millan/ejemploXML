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

    #Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.

def carreteras(carretera,doc):
    provincias = doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%carretera)
    radaresini = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()'%carretera)
    radaresfin = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/PK/text()'%carretera)
    info = [provincias,radaresini,radaresfin]
    return info

    #Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap para ver donde está el radar).

def localizar(carretera,doc):
    cuentaradares = int(doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%carretera))
    latitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)
    longitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)
    info = [cuentaradares,latitud,longitud]
    return info
