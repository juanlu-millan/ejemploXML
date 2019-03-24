    #Mostrar el nombre de las provincias de las que tenemos información sobre radares.

def provincias(doc):
    lista = doc.xpath("//PROVINCIA/NOMBRE/text()")
    return lista

    #Mostrar la cantidad de radares de los que tenemos información.

def radares(doc):
    lista = doc.xpath("count(//RADAR)")
    return lista
