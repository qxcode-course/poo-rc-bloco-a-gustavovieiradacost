class Carro:
    def __init__(self):
        self.pessoas = 0
        self.limite_pessoas = 2
        self.gasolina = 0
        self.tanque_max = 100
        self.km = 0

    def __str__(self):
        return f"pass: {self.pessoas}, gas: {self.gasolina}, km: {self.km}"

    def entrar(self):
        if self.pessoas < self.limite_pessoas:
            self.pessoas += 1
        else:
            print("fail: limite de pessoas atingido")

    def sair(self):
        if self.pessoas > 0:
            self.pessoas -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def abastecer(self, litros):
        self.gasolina += litros
        if self.gasolina > self.tanque_max:
            self.gasolina = self.tanque_max

    def dirigir(self, distancia):
        if self.pessoas == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gasolina == 0:
            print("fail: tanque vazio")
            return
        if self.gasolina >= distancia:
            self.gasolina -= distancia
            self.km += distancia
        else:
            print(f"fail: tanque vazio apos andar {self.gasolina} km")
            self.km += self.gasolina
            self.gasolina = 0


def main():
    carro = Carro()
    while True:
        comando = input().strip().split()
        if len(comando) == 0:
            continue
        print("$" + " ".join(comando))
        acao = comando[0]
        if acao == "end":
            break
        elif acao == "show":
            print(carro)
        elif acao == "enter":
            carro.entrar()
        elif acao == "leave":
            carro.sair()
        elif acao == "fuel":
            litros = int(comando[1])
            carro.abastecer(litros)
        elif acao == "drive":
            distancia = int(comando[1])
            carro.dirigir(distancia)
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
