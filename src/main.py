# Resolve the problem!
import re



def run():
    # Start coding here
    patron = re.compile('[a-z]')

    with open('encoded.txt','r',encoding='utf-8') as file:
        mensaje_codifcado = file.read()
        mensaje_descodificado = ''.join(patron.findall(mensaje_codifcado))
        file.close()
    print(mensaje_descodificado)

if __name__ == "__main__":
    run()