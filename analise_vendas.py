# Projeto: Análise simples de vendas
# Autor: Mara

# Lista de vendas (valores em reais)
vendas = [250, 300, 150, 400, 500, 200]

# Estatísticas básicas
total = sum(vendas)
media = total / len(vendas)
maior = max(vendas)
menor = min(vendas)

print("📊 Relatório de Vendas")
print(f"Total vendido: R$ {total}")
print(f"Média de vendas: R$ {media}")
print(f"Maior venda: R$ {maior}")
print(f"Menor venda: R$ {menor}")


