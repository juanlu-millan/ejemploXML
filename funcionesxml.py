    #Mostrar el nombre de las provincias de las que tenemos información sobre radares.

def provincias(doc):
    lista = doc.xpath("//PROVINCIA/NOMBRE/text()")
    return lista
