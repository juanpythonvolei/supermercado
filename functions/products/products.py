from models.database import *

def add_product(nome:str,tipo:str,sku:int):
  novo_prduto = Produtos(nome,tipo,sku)
  if novo_prduto:
    session.add(novo_prduto)
    session.commit()
    return True
  else:
    return False
  
def delete_product(id:int):
  produto = session.query(Produtos).filter(Produtos.id == id).first()
  if produto:
    session.delete(produto)
    session.commit()
    return True
  else:
    return False
  
def update_product(id:int,nome:str = None,tipo:str = None,sku:int = None):
  produto = session.query(Produtos).filter(Produtos.id == id).first()
  if produto:
    if nome:
      produto.nome_produto = nome
      session.commit()
    if tipo:
      produto.tipo = tipo
      session.commit()
    if sku:
      produto.sku = sku
      session.commit()
    return True
  else:
    return False