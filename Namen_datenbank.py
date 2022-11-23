# 2. Schreibt ein Programm, das Namen speichern und Ausgeben kann. Die Namen sollen ganz simpel in einer Textdatei gespeichert werden.
# Das Programm soll 2 Funktionalitäten haben: 
# 1. Zeige alle Namen und 
# 2. Füge Namen zur Textdatei hinzu. Achtung: Doppelte Einträge sollen nicht eingetragen werden.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///Namensbank.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################

class Name(Base):
    __tablename__ = "Namen"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

def initialize_database():
    Base.metadata.create_all(database)

def database_add_name(name: Name):
    session.add(name)
    session.commit()

def add_new_name():
    print("Einen neuen Freund hinzufügen")
    first_name = input("First name\t:")
    last_name = input("Last name\t:")
    new_friend = Name(first_name=first_name, last_name=last_name)
    database_add_name(new_friend)

def database_get_all_name():
    all_name = session.query(Name).all()
    
    for name in all_name:
        print(f"{name.id} {name.first_name} {name.last_name}")

##################################################################

if __name__ == "__main__":
    initialize_database()

    while True:
        add_new_name()
        exit()
        
database_get_all_name()