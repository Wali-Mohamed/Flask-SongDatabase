import sqlite3

conn=sqlite3.connect(r"c9SQLMusic.db" , check_same_thread=False)
cursor = conn.cursor()
import time



import time

def update():

    # songID to be updated

    idField = input("Enter the songID of the song to be updated: ")

    # Enter the name of the field to be updated (title, artist, genre)

    fieldName = input(

        "Which field would you like to update: (Title, Artist, Genre)? "

    ).title()

    # Enter the value of the fieldName to be updated

    fieldValue = input(f"Enter the new value for the {fieldName} field: ")

    print(f"The new value entered is {fieldValue}")

    # add single quotes around the new field value entered by the user

    fieldValue = "'" + fieldValue +"'"

    # UPDATE songs SET (Title, Artist, Genre) = TitleofSong, ArtistName or songGenre WHERE songID  = idField(12)

    cursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE songID = {idField} ")

    conn.commit()

    print(f"Record {idField} Updated successfully!")

    time.sleep(3)

    #readSongs.read()

#update()
