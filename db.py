"""
    1° - Importa as classes do "models" e salva todas com "table=True" no "metadata" 
    da classe mãe SQLModel

    2° - Cria a tabela das respectivas classes salvas no metadata
    com SQLModel.metadata.create_all(engine) 
"""

# Importe o SQLModel para salvar o metadata e o create_engine para criar a conexão
from sqlmodel import SQLModel, create_engine

# Importe todas as classes da pasta "models", uma por uma
from models import item, teste

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo= True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()