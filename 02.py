"""
Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.
"""

#Solo he considerado copiar lo relevante para el ejercicio

class Persona:
    def __init__(self, _saldo):
        self.nombre = " "
        self.edad = 0
        self._saldo = _saldo
        self.nacionalidad = "Peruana"
        self.monto = 0

    def ingresar_datos(self):
        while True:
            try:
                self.nombre = str(input("\nIngrese su nombre: "))
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Opps¡, debe ingresar su nombre con palabras y su edad con enteros")


class Empleado(Persona):
    def __init__(self, _saldo):
        super().__init__(_saldo)
        self._saldo = _saldo


    def transferecia(self):
        self.monto = int(input("Ingrese el monto a enviar: "))
        self._saldo = self._saldo - self.monto


    def recepcion(self):
        monto_1 = self.monto
        self._saldo = self._saldo - monto_1


persona_1 = Empleado(5000)
persona_1.ingresar_datos()

persona_2 = Empleado(5000)
persona_2.ingresar_datos()

persona_1.transferecia()
print(f"El saldo de la persona 1 es {persona_1._saldo} y el de la persona 2 es {persona_2._saldo}")

