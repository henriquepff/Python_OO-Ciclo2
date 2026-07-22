class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def emitirCertificado(self):
        return f"\n{self.nome} - Certificado genérico de participação."
    

class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso
    
    def emitirCertificado(self):
        return f"\n{self.nome} concluiu o curso de {self.curso} com sucesso."


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade
    
    def emitirCertificado(self):
        return f"\n{self.nome} participou como palestrante na área de {self.especialidade}."
    


def main():
    participantes = []

    while True:
        print("\n===MENU===")
        print("1- Cadastrar participante")
        print("2- Listar participantes")
        print("3- Emitir certificados")
        print("0- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastrar: ")
            print("1- Aluno")
            print("2- Instrutor")

            tipo = input("\nTipo de participante: ")

            nome = input("\nNome: ")
            email = input("Email: ")

            if tipo == "1":
                curso = input("Curso: ")
                aluno = Aluno(nome, email, curso)
                participantes.append(aluno)
                print("\nAluno cadastrado com sucesso.\n")
            elif tipo == "2":
                especialidade = input("Especialidade: ")
                participantes.append(Instrutor(nome, email, especialidade))
                print("\nInstrutor cadastrado com sucesso.\n")
            else:
                print("\nTipo inválido.\n")

        elif opcao == "2":
            if not participantes:
                print("\nNenhum participante cadastrado.\n")
            else:
                print("\n===Participantes Cadastrados===")
                for p in participantes:
                    tipo = "Aluno" if isinstance(p, Aluno) else "Instrutor"
                    print(f"{p.nome} ({tipo}) - {p.email}")

        elif opcao == "3":
            if not participantes:
                print("\nNenhum participante cadastrado.\n")
            else:
                print("\n===Certificados===")
                for p in participantes:
                    print(p.emitirCertificado())
                print()

        elif opcao == "0":
            print("\nEncerrando o programa...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
    
