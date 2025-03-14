from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# Criar um engine para o banco de dados
engine = create_engine(f'sqlite:///models/dados.db',echo=True)

# Definir a classe base do modelo
Base = declarative_base()

# Definir a classe do modelo
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String)
    email = Column(String,unique=True)
    senha = Column(Integer) 
# Criar o banco de dados

class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True,autoincrement=True) 
    nome_produto = Column(String)
    tipo = Column(String)
    sku = Column(Integer)
    preco = Column(Float)

class Estoque(Base):
    __tablename__  = 'estoque'
    id = Column(Integer, primary_key=True,autoincrement=True) 
    sku_produto = Column(Integer)
    quantidade = Column(Integer)
    Rua = Column(String)
    Coluna = Column(String)
    andar = Column(Integer)
    disponibilidade  = Column(BOOLEAN)

class Localizacoes(Base):
    __tablename__ = 'localizacoes'
    id = Column(Integer, primary_key=True,autoincrement=True)  
    Rua = Column(String)
    Coluna = Column(Integer)
    andar = Column(Integer)
    sku_prouduto = Column(Integer)

class Loja(Base):
    __tablename__ = 'loja'
    id = Column(Integer, primary_key=True,autoincrement=True)  
    sku_produto = Column(Integer)
    quantidade = Column(Integer)

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String)
    setor = Column(String)
    cargo = Column(String)
    salario = Column(Float)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()