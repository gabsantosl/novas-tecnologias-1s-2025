# Calculo

turno = input("Turno de Aula:\n" + 
              "M-Matutino\n"+
              "V-Vespertino\n"+
              "N-Noturnp\n")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

match turno:
    case "M":
        pturno = "Estuda no Matutino."
    case "V":
        pturno = "Estuda no Vespertino."
    case "N":
        pturno = "Estuda no Noturno."
    case "_": #operação default
        pturno = "Turno nexistente."

if media < 3: 
    mencao="\nReprovado!"
elif media >= 3 and media < 7:
    mencao="\nRecuperação!"
elif media >= 7 and media < 9:
    mencao="Aprovado."
else: mencao="\nAprovado com louvor!"
