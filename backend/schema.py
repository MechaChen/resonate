import graphene

users_data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
]

# 定義 GraphQL 類型
class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Int()


# 定義查詢類型
class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, id = graphene.Int())

    # 查詢所有使用者
    def resolve_users(parent, info):
        return users_data

    # 根據 id 查詢單一使用者
    def resolve_user(parent, info, id):
        for user in users_data:
            if user["id"] == id:
                return user
        return None


# 定義 Schema
schema = graphene.Schema(query=Query)

