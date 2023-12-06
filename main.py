def calcular_media(n1, n2):
    return (n1 + n2) / 2

def main():
    while True:
        try:
            n1 = float(input("Digite a primeira nota do aluno (ou 'sair' para encerrar): "))
            
            if n1.lower() == 'sair':
                break
            
            n2 = float(input("Digite a segunda nota do aluno: "))

            media = calcular_media(n1, n2)

            print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, media))
        except ValueError:
            print("Por favor, digite notas válidas.")

if __name__ == "__main__":
    main()

#20/10/2023
#(ꈍᴗꈍ)
