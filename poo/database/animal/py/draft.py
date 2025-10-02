# class Animal:
#     def __init__(self, species: str, sound: str):
#         self.species: str = species
#         self.sound: str = sound
#         self.age = 0

#     def __str__(self) -> str:
#         return f"{self.species}:{self.age}:{self.sound}"

# def main():
#     animal = None
#     while True:
#         line: str = input()
#         args: list[str] = line.split(" ")

#         if not args[0]:
#             continue

#         if args[0] == "end":
#             break
#         elif args[0] == "init":
#             if len(args) < 3:
#                 print("fail: falta parametros")
#                 continue
#             species = args[1]
#             sound = args[2]
#             animal = Animal(species, sound)
#         elif args[0] == "show":
#             if animal is not None:
#                 print(animal)
#             else:
#                 print("fail: Nenhum animal criado")
#         else:
#             print("fail: comando desconhecido")

# main()

class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age = 0

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
        
def main():
    animal = None 
    while True:
        line: str = input()
        args: list[str] = line.split(" ")
        print("$" + line)
        if not args[0]:
            continue
        if args[0] == "end":
            break
        elif args[0] == "init":
            if len(args) < 3:
                print("fail: falta parametros")
                continue
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            if animal is not None:
                print(animal)
            else:
                print("fail: Nenhum animal criado")
        else:
            print("fail: comando desconhecido")

main()