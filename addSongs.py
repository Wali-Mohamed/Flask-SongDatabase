import sqlite3

conn=sqlite3.connect(r"c9SQLMusic.db" , check_same_thread=False)
cursor = conn.cursor()
import time

def songs():

    # create an empty list

    



    # title = input("Enter song Title: ")

    # artist = input("Enter Artist: ")

    # genre = input("Enter song Genre: ")

    # append caputured data from user to the songList = []

     # songs.songID is autoincrement and would be added automatically

    "listName.append(variableName=dataEnterd)"
    
    # songList.append(title)

    # songList.append(artist)

    # songList.append(genre)

    #insert the dat from the list into the table songs in

    cursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)", songList)

    conn.commit() # use commit method to write the changes to the database permanently

    print(f"{title} added to Songs Table")# display song name added to the table/database

    time.sleep(3) #delay for 3 seconds then execute the code below
    # read data from the table songs in c9SQLMusic.db database

    # fetch1=cursor.execute("SELECT * FROM songs") # select all songs
    # print(f'first print {fetch1}')
    # row = cursor.fetchall() # fetch all data from the songs table and pass it to the row variable

    # for record in row: # iterate through the row (held data/values) variable

    #      print(record) # print every record in its own line
#songs()
