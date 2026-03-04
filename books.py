from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author' : 'Author One', 'category' : 'science'},
    {'title': 'Title Two', 'author' : 'Author Three', 'category' : 'history'},
    {'title': 'Title Three', 'author' : 'Author Four', 'category' : 'art'},
    {'title': 'Title Four', 'author' : 'Author Two', 'category' : 'computer science'},
    {'title': 'Title Five', 'author' : 'Author Three', 'category' : 'philosophy'},
    {'title': 'Title Six', 'author' : 'Author One', 'category' : 'science'}
]


@app.get("/")
async def home():
    return {'text': 'Welcome to library'}

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title:"str"):
    for book in BOOKS:
        if book['title'] == book_title:
            return book
        else:
            continue
    return {'detail' : 'This book not in this library'}

@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book['category'] == category:
             books_to_return.append(book)
    if len(books_to_return) > 0:
        return {
                'status_code': 200,
                'details' : books_to_return
        }
    else:
        return{
            'status_code' : 404,
            'details' : {'This category not exists in this library'}
        }


@app.get('/books/author/{book_author}')
async def read_books_author(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'] == book_author:
            books_to_return.append(book)
    if len(books_to_return) > 0:
        return {
            'status_code' : 200, 
            'details' : books_to_return    
                }
    else:
        return {
            'status_code' : 404,
            'details' : 'This author not exists in this library'
        }

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'] == book_author and \
            book ['category'] == category:
            books_to_return.append(book)
    if len(books_to_return) == 0:
        return {
            'status_code' : 404,
            'details' : 'Books not found'
            }
    else:
        return {
            'status_code' : 200,
            'details' : books_to_return
            } 

@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'] == updated_book['title']:
            BOOKS[i] = updated_book
            return {'status_code': 200}
        
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'] == book_title:
            BOOKS.pop(i)
            return{'status_code' : 204}
    return{'status_code' : 404}