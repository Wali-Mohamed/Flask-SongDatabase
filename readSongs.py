import sqlite3

conn=sqlite3.connect(r"c9SQLMusic.db" , check_same_thread=False)
cursor = conn.cursor()



def read():

    # read data from the table songs in c9SQLMusic.db database
    #cursor.execute("show tables")
    cursor.execute("SELECT * FROM songs;")  # select all songs

    row = (cursor.fetchall() )  # fetch all data from the songs table and pass it to the row variable
    
    songs=[]
    for record in row:  # iterate through the row (held data/values) variable
        
        songs.append(record)  # print every record in its own line
    
    return songs
    

#print(read())


