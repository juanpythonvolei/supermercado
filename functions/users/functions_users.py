from models.database import *

def add_users(nome:str,email:str,senha:int):
  novo_usuario = Usuario(nome=nome,email=email,senha=senha)
  if novo_usuario:
    session.add(novo_usuario)
    session.commit()
    return novo_usuario
  else:
    return False

def update_users(id:int,nome:str = None,senha:int = None):
  usuario = session.query(Usuario).filter(Usuario.id == id).first()
  if usuario:
    if nome:
      usuario.nome = nome
      session.commit()
      return True
    if senha:
      usuario.senha = senha
      session.commit()
    return True
  else:
    return False
  
def delete_user(email:str):
  usuario = session.query(Usuario).filter(Usuario.email== email).first()
  if usuario:
    session.delete(usuario)
    session.commit()
    return True
  else:
    return False
  
def get_user(email:int):
  usuario = session.query(Usuario).filter(Usuario.email == email).first()
  if usuario:
    return usuario
  else:
    return False