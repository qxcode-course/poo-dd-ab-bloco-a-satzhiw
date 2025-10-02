class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def wringOut(self):
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"

def main():
    toalha = None
    while True:
        # print("$", end=" ")
        line: str = input()
        args: list[str] = line.split (" ")
        print("$" + line)
        if not args[0]:
            continue
        if args[0] == "end":
            break
        elif args[0] == "criar":
            if len(args) < 3:
                print("fail: falta parametros")
                continue
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "mostrar":
            if toalha is not None: 
                print(toalha)
            else:
                print("fail: Nenhuma toalha criada")
        elif args[0] == "seca":
            if toalha is not None:
                if toalha.isDry():
                    print("sim")
                else:
                    print("nao")
            else:
                print("fail: Nenhuma toalha criada")
        elif args[0] == "enxugar":
            if toalha is not None:
                amount = int(args[1])
                toalha.dry(amount)
            else:
                print("fail: Nenhuma toalha criada")
        elif args[0] == "torcer":
            if toalha is not None:
                toalha.wringOut()
            else:
                print("fail: Nenhuma toalha criada")
        else:
            print("fail: comando desconhecido")

main()