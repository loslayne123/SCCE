from banco_dados import BancoDeDados

'''
CREATE TABLE `equipes` (
  `id` int(8) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `localizacao` varchar(15) NOT NULL,
  `potencial` float NOT NULL
);
'''

class Equipe:
    def __init__(self, id, nome, localizacao, potencial):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao
        self.potencial = potencial

    @staticmethod
    def obter_todos():
        bd = BancoDeDados()
        bd.conectar()
        consulta = "SELECT * FROM equipes"
        resultados = bd.executar_consulta(consulta)
        bd.fechar_conexao()
        return [Equipe(*resultado) for resultado in resultados]

    @classmethod
    def criar(cls, nome, localizacao, potencial):
        bd = BancoDeDados()
        bd.conectar()
        consulta = "INSERT INTO equipes (nome, localizacao, potencial) VALUES (%s, %s, %s)"
        bd.executar_consulta(consulta, (nome, localizacao, potencial))
        bd.fechar_conexao()

    def atualizar(self):
        pass

    def apagar(self):
        pass
