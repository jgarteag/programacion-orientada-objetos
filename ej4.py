class Familia:
    """Clase que modela las edades de una familia a partir de la edad de Juan."""

    def __init__(self, edad_juan):
        """Inicializa la familia con la edad de Juan.

        Args:
            edad_juan (int): Edad de Juan (debe ser un número positivo).

        Raises:
            ValueError: Si la edad no es un número positivo.
        """
        if edad_juan <= 0:
            raise ValueError("La edad debe ser un número positivo.")
        self.edad_juan = edad_juan

    def calcular_edad_alberto(self):
        """Calcula la edad de Alberto como 2/3 de la edad de Juan."""
        return (2 / 3) * self.edad_juan

    def calcular_edad_ana(self):
        """Calcula la edad de Ana como 4/3 de la edad de Juan."""
        return (4 / 3) * self.edad_juan

    def calcular_edad_mama(self):
        """Calcula la edad de la mamá como la suma de las edades de los hijos."""
        return self.calcular_edad_alberto() + self.edad_juan + self.calcular_edad_ana()

    def mostrar_edades(self):
        """Muestra en pantalla las edades de todos los miembros de la familia."""
        print(f"Edad de Juan: {self.edad_juan}")
        print(f"Edad de Alberto: {self.calcular_edad_alberto()}")
        print(f"Edad de Ana: {self.calcular_edad_ana()}")
        print(f"Edad de la mamá: {self.calcular_edad_mama()}")

    def __str__(self):
        """Representación en texto del objeto Familia."""
        return (
            f"Familia(Juan={self.edad_juan}, "
            f"Alberto={self.calcular_edad_alberto()}, "
            f"Ana={self.calcular_edad_ana()}, "
            f"Mamá={self.calcular_edad_mama()})"
        )


# Programa principal
if __name__ == "__main__":
    try:
        edad = int(input("Ingrese la edad de Juan: "))
        familia = Familia(edad)
        familia.mostrar_edades()
    except ValueError as e:
        print(f"Error: {e}")