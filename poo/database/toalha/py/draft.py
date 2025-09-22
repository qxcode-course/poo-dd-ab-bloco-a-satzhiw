class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()


    def wringOut(self):
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0

    
    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"

    def main():
        while True:
            toalha = Towel ("", "")
            print("$", end="")
            line: str = imput()
            args: list[str] = line.split (" ")

            if args[0] == "end":
                break
            elif args[0] == "new": #color size
                color = args[1]
                size = args [2]
                tolha = Tolha(color, size)    
            elif args[0] == "show" :
                print(toalha)      
            elif args[0] == "dry": #amount
                amount = int(args[1])
            elif args[0] == "dry": # amount
                amount = int(args[1])
                toalha.dry(amount)
            else:
                print("fail: comando desconhecido")
            
            
            
vermelha = Towel("red", "M")
azul = Towel("blue", "G")

vermelha.dry(5)
vermelha.dry(10)

print (vermelha)