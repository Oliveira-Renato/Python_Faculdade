import os
import sqlite3

db_file = "teste.db"
conector = sqlite3.connect(db_file)
cursor = conector.cursor()

sql = "CREATE TABLE albums(title text, artist text,  release_date text, publisher text,  media_type text)"
cursor.execute(sql)

sql = "INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')"
cursor.execute(sql)
conector.commit()

albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
         ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
         ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
         ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conector.commit()

print("Lista todos os registros na tabela sem formatação:\n")
sql = "SELECT * FROM albums"
cursor.execute(sql)
print(cursor.fetchall())

print("\nLista ordenado pelo artista\n")
sql = "SELECT rowid, * FROM albums ORDER BY artist"
for linha in cursor.execute(sql):
   print(linha)

print("\nResultados de uma consulta com LIKE:\n")
sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
for linha in cursor.execute(sql):
   print(linha)

print("\nResultados de uma consulta direta:\n")
sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("Red")])
print(cursor.fetchall())

if conector:
    conector.close()
    os.remove(db_file)