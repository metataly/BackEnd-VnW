''' Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
Exemplo: ["banana maçã banana laranja maçã maçã"]
Saída: {"banana": 2, "maçã": 3, "laranja": 1}'''

def qtd_elemento(elem):

    dicionario = {}
    palavras = elem.split()
    
    for i in palavras:
        dicionario[i] = elem 
        dicionario[i] = elem.count(i)
    return dicionario

def main():
    
    elementos =  "banana maçã banana laranja maçã maçã"
    
    resp = qtd_elemento(elementos)
    print(resp)

#chamada da função main
if __name__ == "__main__":
    main()
    