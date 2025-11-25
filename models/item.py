from sqlmodel import SQLModel, Field, create_engine

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    qtd: int