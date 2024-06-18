from equipes import Equipe

def main():
    while True:
        print("\n1. Gerenciar Equipes")
        print("2. Sortear Partidas")
        print("3. Visualizar Partidas")
        print("4. Jogar a Próxima Partida")
        print("5. Ver Gráfico de Performance por Equipe")
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            gerencia_equipes()
        elif choice == '2':
            #Sorteia partidas
            pass
        elif choice == '3':
            #Visualizar Partidas
            pass
        elif choice == '4':
            #Jogar a Próxima Partida
            pass
        elif choice == '5':
            #Ver Gráfico de Performance por Equipe
            pass
        elif choice == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def gerencia_equipes():
    while True:
        print("\n1. Ver Equipes Cadastradas")
        print("2. Cadastrar Equipe")
        print("3. Atualizar Equipe")
        print("4. Apagar Equipe")
        print("5. Voltar")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            equipes = Equipe.obter_todos()
            for equipe in equipes:
                print(f"ID: {equipe.id}, Nome: {equipe.nome}, Localização: {equipe.localizacao}, Potencial: {equipe.potencial}")
        elif choice == '2':
            nome = input("Nome do Time: ")
            localizacao = input("Localização (Estado ou País): ")
            potencial = float(input("Potencial (0 a 10): "))
            Equipe.criar(nome, localizacao, potencial)
            equipes = Equipe.obter_todos()
            print(f'Equipe {nome} cadastrada com sucesso')
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()