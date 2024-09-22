import typing

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    @strawberry.field
    def get_books(self) -> typing.List[Book]:
        return [
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
            Book(title="To Kill a Mockingbird", author="Harper Lee"),
            Book(title="1984", author="George Orwell"),
        ]


# 創建 schema
schema = strawberry.Schema(query=Query)

# 創建 FastAPI 應用
app = FastAPI()

# 註冊 GraphQL Router
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "Hello World"}

