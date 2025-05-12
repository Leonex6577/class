#Tapia Hernandez Jose Alejandro 
class Computadoras:
    def __init__ (self, cpu, ram,  grafica, placa_madre):
        self.cpu = cpu
        self.ram = ram
        self.grafica = grafica
        self.placa_madre = placa_madre

gaimer = Computadoras("AMD Ryzen 5 3600X", "ddr4", "Nvidia1660", "Asus")

print(gaimer.cpu)

#El funcionamiento del codigo es el siguiente primero creamos una clase en este ejemplo computadoras y poniendo la definicion de los componentes luego con self para guadarlos y al final  aplicamos eso en una clase con un nombre y los componentes con nombre ´´para al final imprimir
