class Pessoa:
    """A classe representa uma pessoa"""
    __total_pessoas = 0

    def __init__(self, nome: str, idade: int, total_pessoas):
        self.nome = nome
        self.idade = idade

        Pessoa.__total_pessoas += 1

    @classmethod
    def get_total_pessoas(cls):
        return cls.__total_pessoas