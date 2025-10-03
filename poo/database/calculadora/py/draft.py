class Calculadora:
    def __init__(self, batteryMax: int):
        self.display = 0.0 
        self.battery = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def carregar(self, carga: int):
        self.battery += carga
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def gastarBateria(self) -> bool:
        if self.battery > 0:
            self.battery -= 1
            return True 
        else:
            print("fail: bateria insuficiente")
            return False
    
    def soma(self, a: float,  b: float):
        if self.gastarBateria():
            self.display = a + b

    def divisao(self, numA: float, numB: float):
        if not self.gastarBateria():
            return
        if numB == 0:
            print("fail: divisao por zero")
            return
        self.display = numA / numB


def main():
    calculadora = None
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        print("$" + line)
        if not args[0]:
            continue
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora = Calculadora(batteryMax)
        elif args[0] == "show":
            if calculadora is not None: 
                print(calculadora)
        elif args[0] == "charge":
             if calculadora is not None:
                carga = int(args[1])
                calculadora.carregar(carga)
        elif args[0] == "sum":
             if calculadora is not None:
                a = float(args[1])
                b = float(args[2])
                calculadora.soma(a,b)
        elif args[0] == "div":
             if calculadora is not None:
                numA = float(args[1])
                numB = float(args[2])
                calculadora.divisao(numA,numB)
        else:
            print("fail: comando desconhecido")

main()