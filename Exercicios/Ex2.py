''' Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.
Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”) '''

def lista_ordenada(idades):

    return sorted(idades, key=lambda pessoa: pessoa[1])

def main():
    
    pessoas = (("Samuel", 23), ("Karynne", 26), ("Kleber", 21), ("Carol", 28), ("Vinicius", 32))
    
    resp = lista_ordenada(pessoas)
    print(f"A tupla ordenada é {resp}")

#chamada da função main
if __name__ == "__main__":
    main()
    