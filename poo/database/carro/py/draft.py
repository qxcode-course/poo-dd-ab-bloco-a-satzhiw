class Carro:
    def __init__ (self):
        self.passageiros = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
        self.km = 0
    
    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"
    
    def entrar(self):
        if self.passageiros < self.passMax:
            self.passageiros += 1
        else:
            print("fail: limite de pessoas atingido")

    def sair(self):
        if self.passageiros > 0:
            self.passageiros -= 1
        else:
            print("fail: nao ha ninguem no carro")
    
    def abastecer(self, quantidade: int):
        self.gas += quantidade
        if self.gas > self.gasMax: 
            self.gas = self.gasMax

    def dirigir(self, distancia: int):
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro") 
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        distancia_percorrida = min(distancia, self.gas)
        self.km += distancia_percorrida
        self.gas -= distancia_percorrida
        if distancia_percorrida < distancia:
            print(f"fail: tanque vazio apos andar {distancia_percorrida} km")

def main():
    carro = Carro()
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        print("$" + line)
        if not args[0]:
            continue
        if args[0] == "end":
            break
        elif args[0] == "init":
            carro = Carro()
        elif args[0] == "show":
                print(carro)
        elif args[0] == "enter":
                carro.entrar()
        elif args[0] == "leave":
                carro.sair()
        elif args[0] == "fuel":
                quantidade = int(args[1])
                carro.abastecer(quantidade)
        elif args[0] == "drive":
                distancia= int(args[1])
                carro.dirigir(distancia)
        else:
            print("fail: comando desconhecido")

main()