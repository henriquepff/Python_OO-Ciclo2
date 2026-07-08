class AnalisadorString:
    def __init__(self, texto):
        self.texto = texto

    def numero_caracteres(self):
        return len(self.texto)
    
    def em_maiusculo(self):
        return self.texto.upper()
    
    def em_minusculo(self):
        return self.texto.lower()
    
    def contar_vogais(self):
        vogais = "aeiouAEIOUâáêéîíôóûúÁÉÍÓÚÂÊÎÔÛÃÕãõ"
        contador = 0
        for caracter in self.texto:
            if caracter in vogais:
                contador += 1
        return contador

    def contem_ifb(self):
        return "IFB" in self.texto.upper()

def main():
    texto = input("\nDigite um texto: ").strip()
    analisador = AnalisadorString(texto)

    print("\n=====Análise de Texto=====")
    print(f"Número de caracteres: {analisador.numero_caracteres()}")
    print(f"Em maiúsculas: {analisador.em_maiusculo()}")
    print(f"Em minúsculas: {analisador.em_minusculo()}")
    print(f"Número de vogais: {analisador.contar_vogais()}")

    if analisador.contem_ifb():
        print("A substring 'IFB' aparece no texto.")
    else:
        print("A substring 'IFB NÃO aparece no texto.'")

    print()

if __name__=="__main__":
    main()