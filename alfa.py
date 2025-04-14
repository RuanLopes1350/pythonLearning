tarefas = [
    {"nome": "Estudar Python", "completada": False},
    {"nome": "Fazer compras", "completada": True},
    {"nome": "Lavar o carro", "completada": False},
    {"nome": "Ler um livro", "completada": False}
    ]

# funções
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

def listar_tarefas(tarefas):
    print("\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["completada"] else "❌"
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    
    return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome):
    if indice_tarefa < 0 or indice_tarefa >= len(tarefas):
        print("Índice inválido. Tarefa não encontrada.")
        return
    else:
        tarefas[indice_tarefa]["nome"]= novo_nome
        print(f"Tarefa {indice_tarefa} atualizada para '{novo_nome}'")
        return

def completar_tarefa(tarefas, indice_tarefa):
    tarefas[indice_tarefa]["completada"] = True
    print(f"Tarefa {tarefas[indice_tarefa]["nome"]} atualizado para concluído!")
    return

def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("Tarefas completadas deletadas com sucesso!")

# menu
while True: 
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        listar_tarefas(tarefas);
    
    elif escolha == "3":
        listar_tarefas(tarefas)
        indice_tarefa = input("Digite o índice da terefa que deseja atualizar: ")
        if indice_tarefa.isdigit():
            indice_tarefa = int(indice_tarefa) - 1
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
        else:
            print("Por favor digite um número válido!")

    elif escolha == "4":
        indice_tarefa = input("Digite o índice da tarefa que deseja completar: ")
        if indice_tarefa.isdigit():
            indice_tarefa = int(indice_tarefa) - 1
            completar_tarefa(tarefas, indice_tarefa)
        else:
            print("Por favor digite um número válido!")

    elif escolha == "6":
        print("Programa finalizado!")
        break