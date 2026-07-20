class Funcionario:
    def __init__(self, nome, salariobase):
        self.nome = nome
        self.salariobase = salariobase
    
    def calcular_salario(self):
        return self.salariobase
    
    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Salário: R$ {self.calcular_salario():.2f}\n")


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salariobase, comissao):
        super().__init__(nome, salariobase)
        self.comissao = comissao

    def calcular_salario(self):
        return super().calcular_salario() + self.comissao
    
    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Salário Base: R$ {self.salariobase:.2f}")
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcular_salario():.2f}\n")

def main():
    func1 = Funcionario("Maria", 3000.00)
    func2 = FuncionarioComissionado("João", 2500.00, 800.00)

    func1.exibir_dados()
    print("---------------------")
    func2.exibir_dados()


if __name__ == "__main__":
    main()

