class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        print(f"\n{self.nome} cavaleiro da constelação de {self.constelacao}.\n")


class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, nome_golpe):
        super().__init__(nome, constelacao)
        self.nome_golpe = nome_golpe

    def golpe_especial(self):
        print(f"\n{self.nome} executa o {self.nome_golpe}\n")


class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_zodiaco = casa_zodiaco

    def defender_casa(self):
        print(f"\n{self.nome} defende a casa de {self.casa_zodiaco} com honra!\n")


class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, nome_golpe, casa_zodiaco):
        Personagem.__init__(self, nome, constelacao)
        self.nome_golpe = nome_golpe
        self.casa_zodiaco = casa_zodiaco

    def golpe_especial(self):
        print(f"\n{self.nome} executa o {self.nome_golpe}\n")

    def defender_casa(self):
        print(f"\n{self.nome} defende a casa de {self.casa_zodiaco} com honra!\n")



def main():
    personagens = []

    while True:
        print("\n===MENU===")
        print("1- Cadastrar cavaleiro")
        print("2- Listar personagens")
        print("3- Executar habilidades")
        print("0- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nTipo de cavaleiro: ")
            print("1- Cavaleiro de Bronze")
            print("2- Cavaleiro de Ouro")
            print("3- Cavaleiro Híbrido")

            tipo = input("\nTipo de cavaleiro: ")

            nome = input("\nNome: ")
            constelacao = input("Constelação: ")

            if tipo == "1":
                nomeg = input("Nome do golpe: ")
                personagem = CavaleiroDeBronze(nome, constelacao, nomeg)
            elif tipo == "2":
                casa = input("Casa do Zodíaco: ")
                personagem = CavaleiroDeOuro(nome, constelacao, casa)
            elif tipo == "3":
                nomeg = input("Nome do golpe: ")
                casa = input("Casa do Zodíaco: ")
                personagem = CavaleiroHibrido(nome, constelacao, nomeg, casa)
            else:
                print("\nTipo inválido.\n")
                continue

            personagens.append(personagem)
            print("\nCavaleiro cadastrado com sucesso.\n")

        elif opcao == "2":
            if not personagens:
                print("\nNenhum personagem cadastrado.\n")
            else:
                print("\n===Personagens Cadastrados===")
                for p in personagens:
                    p.apresentar()

        elif opcao == "3":
            if not personagens:
                print("\nNenhum personagem cadastrado.\n")
            else:
                print("\n===Habilidades===")
                for p in personagens:
                    print(f"\n{p.nome}: ")
                    if isinstance(p, CavaleiroDeBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()

        elif opcao == "0":
            print("\nEncerrando o programa...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
    