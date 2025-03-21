''' Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
elementos pares contidos nela.
Exemplo: [2,4,10,3,9,7,15,22]
Saída: A soma dos pares é: x '''

def soma_pares(numeros):
    soma = 0;
    
    for numero in numeros:
        soma+=numero

    return soma


def main():
    
    num = [1,2,3,4,5,6,7,8,9,10]
    
    resp = soma_pares(num)
    print(f"A soma dos pares é {resp}")

#chamada da função main
if __name__ == "__main__":
    main()
    