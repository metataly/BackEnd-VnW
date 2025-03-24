'''Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
caracteres da string e os valores representam quantas vezes cada caractere aparece.
Exemplo: [‘Java’, ‘Java’, ‘Ruby’, ‘Javascript’, ‘Ruby’]
Saída: {‘Java’: 2, ‘Ruby’: 2, ‘Javascript’: 1} '''

def qtd_elemento(elem):
    lista = elem.split(' ')
    dicionario = {}
    for i in elem:
        dicionario[i] = lista
        dicionario[i] = lista.count(i)
    return dicionario

def main():
    
    elementos =  "Java Java Ruby Javascript Ruby Ruby"
    
    resp = qtd_elemento(elementos)
    print(resp)

#chamada da função main
if __name__ == "__main__":
    main()
    
