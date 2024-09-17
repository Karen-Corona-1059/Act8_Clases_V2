print("Clases version 2 el constructor \n")

class Perro:

    # funcion constructor
    def __init__(self, color, edad):
      self.color = color
      self.edad = edad
     
    # Funciones creadas por el usuario
    def morder(self):
        print("El perro me mordio")

    def chatperro(self,msj):
       print(f"chat perro: {msj}")

    def chatperra(self,msjp):
       print(f"chat perra: {msjp}")
 
    def dt(self):
       print(f"Color: {self.color} edad: {self.edad}")

# Crear el objeto
chihuas=Perro("Negro",2)

#Llamadas a funciones
chihuas.dt()
chihuas.morder()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola")
chihuas.chatperro("Quieres ser mi rayito de sol en las mañanas?")
chihuas.chatperra("No")

print("\n")