ambientes = ["desenvolvimento", "homologação", "produção"]

print(ambientes[0])
print(ambientes[1])
print(ambientes[2])

"""Ao adicionar numeros negativos, o print acessa a lista de tras para frente"""

print(ambientes[-1])
print(ambientes[-2])
print(ambientes[-3])

execucoes = ["PASSOU", "PASSOU", "FALHOU", "PASSOU"]

ultimo_resultado = execucoes[-1]
print(f"Resultado mais recente:{ultimo_resultado}")

"""corrigindo um e-mail cadastrado errado"""

usuarios = ["kauancruzcerto@gmail.com", "kauanerrrrrado@gmail.com", "layscerto@gmail.com"]
print(usuarios)
"""Print com o email errado"""

usuarios[1] = "kauanerrado@gmail.com"
print (usuarios)
"""print com email corrigido"""

"""adicionando novos usuarios na lista"""
usuarios.append("kauanadd1@gmail.com")
usuarios.append("laysadd1@gmail.com")

print(usuarios)

"""adicionando novos usuarios na lista, mas em desejadas"""
usuarios.insert(0, "admin@gmail.com")
print(usuarios)

"""removendo usuarios da lista"""
usuarios.remove("admin@gmail.com")
usuarios.pop()
print(usuarios)

"""descobrindo o tamanho da lista"""
resultados_api = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

total = len(resultados_api)

print(f"total de resultados:{total}")

esperado = 5

if len(resultados_api) == esperado:
    print("Quantidade de resultados correra!")
else:
    print(f"Esperava {esperado}, mas veio {len(resultados_api)}")

"""Utilizando loops em listas"""
ambientes = ["desenvolvimento", "homologação", "produção"]

for ambiente in ambientes:
    print(f"Testando em {ambiente}")

"""verificando se um item existe na lista"""""
codigos_sucesso = [200, 201, 204]
codigo_recebido = 201

if codigo_recebido in codigos_sucesso:
    print(f"código {codigo_recebido} é um código de sucesso!")
else:
    print(f"Código {codigo_recebido} não era o esperado.")

"""Verificando se um item não existe na lista"""
erros_criticos = [500, 502, 503]
codigo = 401

if codigo not in erros_criticos:
    print(f"Código {codigo} não é um erro critico")
else:
    print(f"Código {codigo} é um erro critico")