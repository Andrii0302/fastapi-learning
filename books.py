from fastapi import FastAPI
from fastapi import Body, Path, Query
app=FastAPI()
BOOKS = [
    {'title':'Title One', 'author':'Author One', 'category':'science'},
    {'title':'Title Two', 'author':'Author Two', 'category':'science'},
    {'title':'Title Three', 'author':'Author Three', 'category':'history'},
    {'title':'Title Four', 'author':'Author Four', 'category':'math'},
    {'title':'Title Five', 'author':'Author Five', 'category':'math'},
    {'title':'Title Six', 'author':'Author Two', 'category':'math'},
]
@app.get('/books')
async def read_all_books():
    return BOOKS

# path parameters
@app.get('/books/{book_title}')
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
# query parameters
@app.get('/books/')
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
@app.get('/books/byauthor/')
async def read_book_by_author(book_author:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
@app.get('/books/{book_author}/')
async def read_category_by_query(book_author:str, category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
# post request, have to pass body 
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

