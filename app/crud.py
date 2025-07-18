from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import or_

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db_book.title = book.title
    db_book.author = book.author
    db_book.price = book.price
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book

def search_books(db: Session, q: str):
    return db.query(models.Book).filter(
        or_(
            models.Book.title.ilike(f"%{q}%"),
            models.Book.author.ilike(f"%{q}%")
        )
    ).all()
