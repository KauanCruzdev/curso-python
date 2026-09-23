usuario = {
    "nome": "Kauan",
    "idade": "22",
    "ativo": True,
}
print(usuario)

"""acessando valores"""

print(usuario["nome"])
print(usuario["idade"])

'''adicionando valores'''

usuario["cidade"] = "São Paulo"
print(usuario)

"""alterando valores"""

usuario["idade"] = 31
print(usuario)

"""removendo valores"""

item_removido = usuario.pop("cidade")
print(f"O item removido foi {item_removido}")
print(usuario)

"""descobrindo o tamanho"""
print(len(usuario))

"""percorrendo usuarios"""
for valor in usuario:
    print(valor)

"""verificando se uma chave existe"""
if "nome" in usuario:
    print("chave encontrada")