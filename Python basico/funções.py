def classificar_status_code(codigo):

    if 200 <= codigo < 300:
        print(f"Status {codigo}: sucesso")
    elif 400 <= codigo < 500:
        print(f"Status {codigo}: erro do cliente")
    elif 500 <= codigo < 600:
        print(f"Status {codigo}: erro do servidor")

classificar_status_code(201)
classificar_status_code(404)
classificar_status_code(500)

#Retorno de uma função

def calcular_taxa_sucesso(total, aprovados):
    if total == 0:
        return 0
    return (aprovados / total) * 100

taxa = calcular_taxa_sucesso(total= 10, aprovados= 7)
print(taxa)

print(f"Taxa de sucesso: {taxa}%")