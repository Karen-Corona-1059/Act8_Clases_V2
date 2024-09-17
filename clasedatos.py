print("\n")
class Infomacion:

    def mi_lista(self):
        lista_NPerro=["Fulgensia","Filomeno","Panfilo"]
        for x in lista_NPerro:
            print(x)
    
    def tupla(self):
        razas=("chihuas","Doberman", "Pastor australiano")
        for x in razas:
            print(x)

    def conjunto(self):
        toxico={"chocolate","nuez", "semillas de manzana"}
        for x in toxico:
            print(x)

    def diccionario(self):
        perritos = {
            "Nombre:" : "Panfilo",
            "Edad:" : "10 años",
            "Raza:" : "Doberman"
        }
        for x,z in perritos.items ():
            print(x,z)

# Creando el objeto

datos=Infomacion()
print("Listado de nombres de perros")
datos.mi_lista()
print("\n")

print("Tupla de razas de perros")
datos.tupla()
print("\n")

print("conjunto de alimentos toxicos para perros")
datos.conjunto()
print("\n")

print("Diccionario perritos")
datos.diccionario()


print("\n")