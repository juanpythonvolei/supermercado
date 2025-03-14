from models.database import *

def add_products_to_storage(sku:int,quantidade:int,rua:str,coluna:str,andar:int,disponibiliade=True):
  nova_adicao  = Estoque(sku,quantidade,rua,coluna,andar,disponibiliade)
  if nova_adicao:
    session.add(nova_adicao)
    session.commit()
    return True
  else:
    return False
  
def update_products_on_storage(sku:int,id_localizacao:int,quantidade:int,rua:str = None,coluna:str = None,andar:int = None,disponibilidade=True):
  id_localizacao_atual = session.query(Estoque).filter(Estoque.sku_produto == sku,Estoque.id == id_localizacao).first()
  nova_localizacao_produto = session.query(Estoque).filter(Estoque.sku_produto == sku,Estoque.rua==rua,Estoque.Coluna==coluna,Estoque.andar==andar).first()
  if sku and id_localizacao and quantidade and rua and coluna and andar:
    if nova_localizacao_produto:
      nova_localizacao_produto.quantidade += quantidade
      id_localizacao_atual.quantidade -= quantidade
      session.commit()
    else:
      session.add(
        Estoque(sku,quantidade,rua,coluna,andar,disponibilidade)
      )
      id_localizacao_atual.quantidade -= quantidade
      session.commit()
    return True
  else:
    return False

def delete_products_on_storage(sku:int,id_storage:int):
  localizacao = session.query(Estoque).filter(Estoque.id == id_storage).first()
  if localizacao:
    session.delete(localizacao)
    session.commit()
    return True
  else:
    return False

def get_products_on_storage(sku:int):
  produtos = session.query(Estoque).filter(Estoque.sku_produto == sku).all()
  if produtos:
    return produtos
  else:
    return False