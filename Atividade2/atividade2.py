def calcular_soma_produto(idade_homem1, idade_homem2, idade_mulher1, idade_mulher2):
    # Validação: Verificar se todas as idades são inteiros positivos
    idades = [idade_homem1, idade_homem2, idade_mulher1, idade_mulher2]
    if not all(isinstance(idade, int) and idade > 0 for idade in idades):
        return "Erro: Todas as idades devem ser números inteiros positivos."
    
    # Identificar o homem mais velho e o mais novo
    homem_mais_velho = max(idade_homem1, idade_homem2)
    homem_mais_novo = min(idade_homem1, idade_homem2)
    
    # Identificar a mulher mais velha e a mais nova
    mulher_mais_velha = max(idade_mulher1, idade_mulher2)
    mulher_mais_nova = min(idade_mulher1, idade_mulher2)
    
    # Calcular a soma do homem mais velho com a mulher mais nova
    soma = homem_mais_velho + mulher_mais_nova
    
    # Calcular o produto do homem mais novo com a mulher mais velha
    produto = homem_mais_novo * mulher_mais_velha
    
    return soma, produto

def obter_idades():
    try:
        idade_homem1 = int(input("Digite a idade do primeiro homem: "))
        idade_homem2 = int(input("Digite a idade do segundo homem: "))
        idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
        idade_mulher2 = int(input("Digite a idade da segunda mulher: "))
        
        return idade_homem1, idade_homem2, idade_mulher1, idade_mulher2
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros.")
        return None

# Função principal para execução
def main():
    idades = obter_idades()
    if idades is not None:
        soma, produto = calcular_soma_produto(*idades)
        print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
        print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")

if __name__ == "__main__":
    main()
