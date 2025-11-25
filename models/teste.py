from sqlmodel import SQLModel, Field

class Teste(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    qtd: int | None = None