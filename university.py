class Universidade:
    total_estudantes = 0
    total_professores = 0
    
    @classmethod
    def matricular_estudante(cls):
        cls.total_students += 1
        
    @classmethod
    def contratar_professor(cls):
        cls.total_professors += 1
        
    @classmethod
    def obter_total_pessoas(cls):
        return cls.total_professors + cls.total_students