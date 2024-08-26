# Calcular médias e filtrar aprovados

# Entrada: Uma lista de dicionários, cada um representando um estudante com as chaves nome, notas (uma lista de notas) e curso.

# dicionario = {nome:  str, notas: float, curso: str}
# lista com esses dicionarios

# Exemplo:
# 		Entrada:
# 		[{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"},
# 		{"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"},
# 		{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]
		
# 		Saída:		
# 		[{"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação", "media": 9.0},
# 		{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática", "media": 8.33}]


def calcular_medias_e_filtrar(lista):
    def medias(lista):
        for dicionario in lista:
            dicionario.update({"média":sum(list(dicionario.items())[1][1])/3})
        print(lista)
        return lista
    lista_com_medias = medias(lista)

    def filtro(lista_com_medias):
        for dicionario in lista_com_medias:
            return list(dicionario.values())[-1] >= 7

    for item in filter(filtro, lista_com_medias):
        return item


print(calcular_medias_e_filtrar([{"nome": "Alice", "notas": [8.5, 9.0, 7.5], "curso": "Matemática"}, {"nome": "Bob", "notas": [6.0, 5.5, 7.0], "curso": "Física"}, {"nome": "Charlie", "notas": [9.5, 8.0, 9.0], "curso": "Computação"}]))
