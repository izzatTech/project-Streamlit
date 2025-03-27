import streamlit as st
import sqlite3

# 📌 Function to connect to the database
def get_connection():
    conn = sqlite3.connect("library.db")
    return conn

# 📌 Check if the table exists; if not, create it
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# 📌 Function to add a new book
def add_book(title, author, genre, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books_record (title, author, genre, year) VALUES (?, ?, ?, ?)", 
                   (title, author, genre, year))
    conn.commit()
    conn.close()

# 📌 Function to fetch all books
def get_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books_record")
    books = cursor.fetchall()
    conn.close()
    return books

# 📌 Streamlit UI
st.title("📚 Personal Library Manager")

# 🔹 Create the table first
create_table()

# 🔹 Section to display all books
st.subheader("📖 All Books in Library")
books = get_books()
if books:
    for book in books:
        st.text(f"{book[0]}. {book[1]} by {book[2]} ({book[3]}, {book[4]})")
else:
    st.write("📌 No books found. Please add a new book.")

# 🔹 Section to add a new book
st.subheader("➕ Add a New Book")
title = st.text_input("Title")
author = st.text_input("Author")
genre = st.text_input("Genre")
year = st.number_input("Year", min_value=1000, max_value=9999, step=1)

if st.button("Add Book"):
    if title and author:
        add_book(title, author, genre, year)
        st.success("✅ Book added successfully!")
        st.experimental_rerun()
    else:
        st.error("❌ Title and Author are required!")