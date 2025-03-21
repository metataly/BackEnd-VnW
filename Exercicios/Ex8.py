'''Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
pode ser lida da mesma forma de trás para frente) e False caso contrário.
Exemplo:
entrada = "radar"
Saída: True'''

def palindromo(palavra):
    if palavra == palavra[::-1]: #[::-1] inverte a strg
        return True;
    else:
        return False;
    

def main():
    
    palavra = "arara"
    resp = palindromo(palavra)
    print(resp)

#chamada da função main
if __name__ == "__main__":
    main()

