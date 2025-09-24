class Animal:
    def __init__(self, species, sound):
        self.species = species 
        self.sound = sound
        self.age = 0

    def __init__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
    gato = Animal("gato", "miau")
    print(gato)

    cachorro = Animal("cachorro","auau")
    print(cachorro)

    galinha = Animal("galinha", "cocorico")
    print("galinha")
