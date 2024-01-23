# É necessário importar a variável DB
from database import db

class Diario(db.Model):
  __tablename__= "diario"
  id = db.Column(db.Integer, primary_key = True)
  titulo = db.Column(db.String(100))
  disciplina = db.Column(db.String(100))

  def __init__(self, titulo, disciplina):
    self.titulo = titulo
    self.disciplina = disciplina

  
  @classmethod
  def post_user(cls, titulo, disciplina):
    print(cls)
    novo_diario = cls(titulo=titulo, disciplina=disciplina)
    db.session.add(novo_diario)
    db.session.commit()
    return novo_diario