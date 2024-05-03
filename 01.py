"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""

from datetime import datetime, date

class Persona:
    def __init__(self):
        self.nombre = " "
        self.edad = 0
        self.nacionalidad = "Peruana"

    def ingresar_datos(self):
        while True:
            try:
                self.nombre = str(input("\nIngrese su nombre: "))
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Opps¡, debe ingresar su nombre con palabras y su edad con enteros")

    def cumpleaños(self):
        self.edad = self.edad + 1
        return self.edad

    def fecha_registro(self):
        self.fecha = date.today()
        self.tiempo = datetime.now()
        self.hora = self.tiempo.hour
        self.minuto = self.tiempo.minute

        print(f"El registo fue el día {persona_1.fecha} a las {persona_1.hora} horas con {persona_1.minuto} minutos")


persona_1 = Persona()
persona_1.ingresar_datos()
persona_1.cumpleaños()
persona_1.cumpleaños()
print(f"{persona_1.nombre} tiene actualmente {persona_1.edad}")
persona_1.fecha_registro()

persona_2 = Persona()
persona_2.ingresar_datos()
persona_2.cumpleaños()
persona_2.cumpleaños()
persona_2.cumpleaños()
persona_2.cumpleaños()
print(f"{persona_2.nombre} tiene actualmente {persona_2.edad}")
persona_2.fecha_registro()