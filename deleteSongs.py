import sqlite3

conn=sqlite3.connect(r"c9SQLMusic.db" , check_same_thread=False)
cursor = conn.cursor()

import readSongs as readSongs
import time

def delete():
    # songID to be deleted
    idField = input("Enter the songID of the song to be deleted: ")
    # Method 1
    # DELETE FROM songs WHERE songID=1, OR 2, OR 4...
    cursor.execute("DELETE FROM songs WHERE songID=" + idField)
    conn.commit()
    print(
        f"Record {idField} deleted from Songs Table"
    )  # display songID deleted from the Songs table/database

    time.sleep(3)  # delay for 3 seconds then execute the code below

    "filename.subroutineName()"

    readSongs.read() # invoke the read subroutine for the read songs file/app

#delete()