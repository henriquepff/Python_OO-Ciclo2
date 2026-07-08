class Criptografia:
    def __init__(self, texto):
        self.texto = texto

    def criptografar(self):
        substituicoes = {
            "a": "4", "A": "4",
            "e": "3", "E": "3",
            "i": "1", "I": "1",
            "o": "0", "O": "0",
            "u": "8", "U": "8"
        }

        texto_criptografado = ""

        for caractere in self.texto:
            if caractere in substituicoes:
                texto_criptografado += substituicoes[caractere]
            else:
                texto_criptografado += caractere
        return texto_criptografado



def main():
    texto = input("\nDigite um texto para criptografar: ")
    criptografia = Criptografia(texto)

    resultado = criptografia.criptografar()
    print("\nFrase criptografada: ")
    print(resultado)
    print()Tchau 



if __name__=="__main__":
    main()