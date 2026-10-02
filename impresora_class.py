class Impresora:
    
    def _init_(self, filamento_color, temperatura):
        self.filamento_color = filamento_color
        self.temperatura = temperatura
        
    def Imprimir(self):
        print(f"La placa tiene una temperatura de{self.temperature} y la impresion sera de color: {self.color}")