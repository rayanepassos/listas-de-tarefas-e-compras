print("O programa tem como finalidade: Dois tipos de listas, uma de compras e a outra é apenas uma lista de tarefas simples.")

def lista_compras():
    compras = []

    while True:
        produto = input("\nDigite o nome do produto (ou 'sair' para finalizar): ")
        if produto.lower() == 'sair':
            break
        
        quantidade = int(input(f"\nDigite a quantidade de {produto}: "))
        preco = float(input(f"\nDigite o preço de {produto}: R$ "))
        compras.append((produto, quantidade, preco))

    total = 0
    print("\nLista de Compras:")
    for item in compras:
        produto, quantidade, preco = item
        total_item = quantidade * preco
        print(f"{produto} - Quantidade: {quantidade}, Preço unitário: R$ {preco:.2f}, Total: R$ {total_item:.2f}")
        total += total_item

    print(f"\nTotal a pagar: R$ {total:.2f}")

def lista_tarefas():
    tarefas = []

    while True:
        print("\n1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Mostrar lista de tarefas")
        print("4. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            tarefa = input("\nDigite uma tarefa: ")
            tarefas.append({"tarefa": tarefa, "concluida": False})
        elif escolha == '2':
            if not tarefas:
                print("Nenhuma tarefa para marcar como concluída.")
                continue
            
            for i, tarefa in enumerate(tarefas):
                status = "Concluída" if tarefa["concluida"] else "Não concluída"
                print(f"{i + 1}. {tarefa['tarefa']} - {status}")
            
            tarefa_num = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            
            if 0 <= tarefa_num < len(tarefas):
                tarefas[tarefa_num]["concluida"] = True
                print(f"Tarefa '{tarefas[tarefa_num]['tarefa']}' marcada como concluída.")
            else:
                print("Número de tarefa inválido.")
        elif escolha == '3':
            if not tarefas:
                print("Nenhuma tarefa na lista.")
            else:
                print("\nLista de Tarefas:")
                for tarefa in tarefas:
                    status = "Concluída" if tarefa["concluida"] else "Não concluída"
                    print(f"- {tarefa['tarefa']} ({status})")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("\nEscolha o tipo de lista:")
    print("\n1. Lista de Compras")
    print("2. Lista de Tarefas do Dia a Dia")
    
    escolha = input("\nDigite o número da opção desejada: ")

    if escolha == '1':
        lista_compras()
    elif escolha == '2':
        lista_tarefas()
    else:
        print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()
