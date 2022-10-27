from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    # Foreignkeys
    language_id = Column(Integer, ForeignKey("languages.id"))


def initialize_database():
    """
    Initializes the database and creates all tables.
    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def show_menu():
    """
    Displays a menu.
    """

    MENU_TEXT = """
    Menu: 
    - (A)dd new Friend
    - (L)ist all Friends
    - (D)eleat a Friend
    - (E)xit
    """
    print(MENU_TEXT)


def get_users_menu_input():
    menu_choice = input("Choose menue option: ")

    if menu_choice == "A":
        add_new_friend()
    elif menu_choice == "E":
        exit(1)
    elif menu_choice == 'L':
        database_get_all_friends()
    elif menu_choice == 'D':
        database_delete_friend()

def database_delete_friend():
    """
    Database command to delete a  friend.
    """
    id = input("Geben Sie die Nummer ein des Freundes den sie löschen wollen: ")
    session.execute(f"DELETE FROM friends WHERE id = {id}") #SQL
    
    session.query(Friend).filter(Friend.id == id).delete(synchronize_session='evaluate')
    session.commit()#query

def add_new_friend():
    """
    Asks the user for the information about the new friend. 
    Adds the friend to the database.
    """
    print("Einen neuen Freund hinzufügen")
    first_name = input("First name\t:")
    last_name = input("Last name\t:")
    new_friend = Friend(first_name=first_name, last_name=last_name)
    database_add_friend(new_friend)

def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    ORM = Object Relational Mapper
    """
    session.add(friend)
    session.commit()

def database_add_language(language: Language):
    """
    Database command to add a new language.
    """
    session.add(language)
    session.commit()

def database_get_all_friends():
    """
    Database command to get all friends.
    `all_friends = session.query(Friend).all()` is a query call made with the sqlalchemy ORM. 
    The SQL query that is made is: `SELECT * FROM friends;`
    Alternative to this with raw sql:
    `all_friends_raw = session.execute("SELECT * FROM friends;").fetchall()`
    """
    all_friends = session.query(Friend).all()
    
    for friend in all_friends:
        print(f"{friend.id} {friend.first_name} {friend.last_name}")


# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

#Beispiel 0
    #new_language = Language(name = 'Deutsch')
    #database_add_language(new_language)

    while True:
        show_menu()
        get_users_menu_input()