'''Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
inteiros. A função deve combinar os dicionários somando os valores das chaves que
aparecem em ambos.
Exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
Saída: {"a": 3, "b": 7, "c": 5, "d": 7}'''

def soma_dic(dic1, dic2):

    dicionario = {}
    
    for i in dic1:
        if i in dic2:
            dicionario[i] = dic1[i] + dic2[i] 
        else:
            dicionario[i] = dic1[i]
      
    for i in dic2:
        if i in dic1:
            dicionario[i] = dic1[i] + dic2[i] 
        else:
            dicionario[i] = dic2[i]      
    
    return dicionario

def main():
    
    d1 = {"a": 2, "b": 3, "c": 5}
    d2 = {"a": 1, "b": 4, "d": 7}
    
    resp = soma_dic(d1, d2)
    print(resp)

#chamada da função main
if __name__ == "__main__":
    main()
    