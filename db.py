"""
    1° - Importa as classes do "models" e salva todas com "table=True" no "metadata" 
    da classe mãe SQLModel

    2° - Cria as tabelas e o banco apenas se o arquivo for executado
"""

# Importa o SQLModel, atualizando o metadata
from sqlmodel import SQLModel, create_engine, Session

# Importe as classes da pasta "models", uma por uma
# Com isso, salva cada uma no metadata
from models import item

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo= True)
session = Session(engine)

# Criar as tabelas e o banco
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()