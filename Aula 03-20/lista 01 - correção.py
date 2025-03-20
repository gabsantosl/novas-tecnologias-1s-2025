# questão 01
print("""
        ******     ***
        *    *    *   *
        *    *    *   *
        ******     ***
""")

# questão 02
numero = input("Digite um  número>: ")

for num in numero:
    print(num, end=" ")

# questão 03
print("Digite os pontows do plano" +
                      "cartesiano - P1(x,y) e P2(x,y): ")

x1= float(input("x1: "))
x2= float(input("x2: "))
y1= float(input("y1: "))
y2= float(input("y2: "))

dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)

print(f"Distância:{dist}")

# questão 04
frase = (input("Digite uma frase: "))
print(f"Na frase \"{frase}\" tem\n",
      f"a ou A: {frase.count("a")+frase.count("A")}\n"+
      f" e ou E: {frase.count("e")+frase.count("E")}\n"+
      f" i ou I: {frase.count("i")+frase.count("I")}\n"+
      f" o ou O: {frase.count("o")+frase.count("O")}\n"+
      f" u ou U: {frase.count("u")+frase.count("U")}\n")

# questão 05
msg = input("Digite a sua mensagem: ")
msgCript=""
for digito in msg:
    msgCript+=str((int(digito)+7)%10)

""" msg[2]= str((int(msg[0])+7)% 10)
msg[3]= str((int(msg[1])+7)% 10)
msg[0]= str((int(msg[2])+7)% 10)
msg[1]= str((int(msg[3])+7)% 10) """

print("Criptografada: " +
                    msgCript[2]+msgCript[3]+msgCript[0]+msgCript[1])

msgDesCript=""
for digito in msgCript:
    msgDesCript++str((int(digito)+7)%10)
