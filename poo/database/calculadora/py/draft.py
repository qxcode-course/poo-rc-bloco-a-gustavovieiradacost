class Calculadora:
    def __init__(self, batteryMax):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax  
        
    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
            
    def sum(self, a, b):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.display = a + b
        self.battery -= 1

    def div(self, numerator, denominator):
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        if denominator == 0:
            print("fail: divisao por zero")
            self.battery -= 1
            return
        self.display = numerator / denominator
        self.battery -= 1


def main():
    calc = None

    while True:
        comando = input().strip().split()
        if len(comando) == 0:
            continue

        # Imprime o comando digitado com $
        print("$" + " ".join(comando))

        acao = comando[0]

        if acao == "end":
            break
        elif acao == "init":
            calc = Calculadora(int(comando[1]))
        elif acao == "show":
            print(calc)
        elif acao == "charge":
            calc.charge(int(comando[1]))
        elif acao == "sum":
            a = float(comando[1])
            b = float(comando[2])
            calc.sum(a, b)
        elif acao == "div":
            num = float(comando[1])
            den = float(comando[2])
            calc.div(num, den)
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()        