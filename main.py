from fastapi import FastAPI

app = FastAPI()

# @app.get("/hello/")
# async def hello():
#     return({"Message":"Hello world"})

data = {
    "id": "0ee1cc2a-5a1a-4ece-91d4-7db8abcf41b9",
    "title": "Sapiens",
    "author": "Yuval Noah Harrari",
    "genre": "non-fiction",
    "yearPublished": 1997,
    "createdAt": "2023-03-22T09:17:03.816Z"
}


@app.get("/books/{id}")
async def get_books():
    return data

# async def get_book(id: int):
#     for book in data:
#         if(book['id'] == id):
#             return (book)
#     return{"Message")