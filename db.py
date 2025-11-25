"""
    Salva as classes com "table=True" no atributo "metadata" da classe mãe SQLModel
    
    Esse arquivo tem que ser executado antes de SQLModel.metadata.create_all(engine), caso contrário,
    o atributo metadata estará vazio

    Importe para o "main.py" assim: from db import engine, SQLModel
    Em seguida, execute o SQLModel.metadata.create_all(engine)
"""

# Importe o SQLModel para salvar o metadata e o create_engine para criar a conexão
from sqlmodel import SQLModel, create_engine

# Importe todas as classes da pasta "models", uma por uma
from models import item

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo= True)