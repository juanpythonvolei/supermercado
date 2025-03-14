from models.database import *

class Store:
  def __init__(self,session):
    self.banco = session

  def add_product_on_store(self,sku_produto:int,quantidade:int,):
    self.banco.add(Loja(sku_produto,quantidade))
    self.banco.commit()
    return True
  
  def add_employee_on_store(self,nome:str,setor:str,cargo:str,salario:float):
    novo_funcionario = Funcionario(nome,setor,cargo,salario)
    if novo_funcionario:
      self.banco.add(
        novo_funcionario
      )
      self.banco.commit()
      return True
    else:
      return False
    
  def delete_product_from_store(self,sku_produto:int):
    produto = self.banco.query(Loja).filter(Loja.sku_produto == sku_produto).first()
    if produto:
      self.banco.delete(produto)
      self.banco.commit()
      return True
    else:
      return False
    
  def get_product_on_store(self,sku:int):
    produto = self.banco.query(Loja).filter(Loja.sku_produto == sku).first()
    if produto:
      return produto
    else:
      return False