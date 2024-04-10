import sqlite3

# Function to create the database if it doesn't exist
def create_database():
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tblfilms 
                (filmID INTEGER PRIMARY KEY, title TEXT, yearReleased INTEGER, rating TEXT, duration INTEGER, genre TEXT)''')
    conn.commit()
    conn.close()

# Function to print all records in tblfilms
def print_all_records():
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tblfilms")
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()

# Function to add a record to tblfilms
def add_record(title, year, rating, duration, genre):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
              (title, year, rating, duration, genre))
    conn.commit()
    conn.close()

# Function to delete a record from tblfilms
def delete_record(film_id):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("DELETE FROM tblfilms WHERE filmID = ?", (film_id,))
    conn.commit()
    conn.close()

# Function to update a record in tblfilms
def update_record(film_id, title, year, rating, duration, genre):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("UPDATE tblfilms SET title=?, yearReleased=?, rating=?, duration=?, genre=? WHERE filmID=?",
              (title, year, rating, duration, genre, film_id))
    conn.commit()
    conn.close()

# Function to print details of all films
def print_all_films():
    print_all_records()

# Function to print all films of a particular genre
def print_films_by_genre(genre):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tblfilms WHERE genre=?", (genre,))
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()

# Function to print all films of a particular year
def print_films_by_year(year):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tblfilms WHERE yearReleased=?", (year,))
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()

# Function to print all films of a particular rating
def print_films_by_rating(rating):
    conn = sqlite3.connect('filmflix.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tblfilms WHERE rating=?", (rating,))
    records = c.fetchall()
    for record in records:
        print(record)
    conn.close()

# Main function to run the application
def main():
    create_database()

    while True:
        print("\nOptions menu")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Update a record")
        print("4. Print all records")
        print("5. Print details of all films")
        print("6. Print all films of a particular genre")
        print("7. Print all films of a particular year")
        print("8. Print all films of a particular rating")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            year = int(input("Enter year released: "))
            rating = input("Enter rating: ")
            duration = int(input("Enter duration: "))
            genre = input("Enter genre: ")
            add_record(title, year, rating, duration, genre)
            print("Record added successfully!")
        elif choice == '2':
            film_id = int(input("Enter film ID to delete: "))
            delete_record(film_id)
            print("Record deleted successfully!")
        elif choice == '3':
            film_id = int(input("Enter film ID to update: "))
            title = input("Enter updated title: ")
            year = int(input("Enter updated year released: "))
            rating = input("Enter updated rating: ")
            duration = int(input("Enter updated duration: "))
            genre = input("Enter updated genre: ")
            update_record(film_id, title, year, rating, duration, genre)
            print("Record updated successfully!")
        elif choice == '4':
            print_all_records()
        elif choice == '5':
            print_all_films()
        elif choice == '6':
            genre = input("Enter genre to filter: ")
            print_films_by_genre(genre)
        elif choice == '7':
            year = int(input("Enter year to filter: "))
            print_films_by_year(year)
        elif choice == '8':
            rating = input("Enter rating to filter: ")
            print_films_by_rating(rating)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
