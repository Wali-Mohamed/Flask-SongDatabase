import numpy as np
import seaborn as sns
from flask import Flask, request, jsonify, render_template
#from readSongs import *
import readSongs
import sqlite3

conn=sqlite3.connect(r"c9SQLMusic.db" , check_same_thread=False)
cursor = conn.cursor()



# Create flask app
flask_app=Flask(__name__)
#flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("menu.html")
    #return render_template("styles.css")

@flask_app.route("/read", methods = ["POST"])
def read():
    songs=readSongs.read()
    
    # return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
    return render_template("list.html", read_songs = songs )

@flask_app.route("/add" , methods=['POST'])
def add():
   return render_template("add.html")
@flask_app.route("/list", methods = ["POST"])
def append():
    songList=[]
    title=request.form['title']
    songList.append(title)
    artist=request.form['artist']
    songList.append(artist)
    genre=request.form['genre']
    songList.append(genre)
    songList
    cursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)", songList)
    conn.commit() # use commit method to write the changes to the database permanently
    songs=readSongs.read()
    
    # return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
    return render_template("list.html", songlist=f"{title} added to Songs Table", read_songs = songs)

# @flask_app.route("/updatepage", methods = ["POST", 'GET'] )
# def updatepage():
    


#     return render_template("update.html")

@flask_app.route("/updatefield1", methods = ["POST", 'GET'] )
def updatefield1():
    
    return render_template("updating.html")
@flask_app.route("/updatefield2", methods = ["POST", 'GET'] )
def updatefield2():
    songID = request.form["songID"]
    field = request.form["ufield"]
    updatefield=field.title()
    
    

    


    return render_template("updating.html", updatefield=updatefield, songID=songID)

@flask_app.route("/update" , methods=['POST' , 'GET'])
def update():
    idField = request.form["songID"]
    fieldName1=request.form['ufield']
    fieldValue=request.form['fieldvalue']
    #idField = request.form.get("songID")
    fieldValue = "'" + fieldValue +"'"
    cursor.execute(f"UPDATE songs SET {fieldName1.title()} = {fieldValue} WHERE songID = {idField}")
    conn.commit()
    songs=readSongs.read()


    return render_template("list.html", updateMessage=f"The new value entered is {fieldValue}", read_songs=songs)

@flask_app.route("/deletepage", methods = ["POST", 'GET'] )
def deletereq():
    


    return render_template("delete.html")



@flask_app.route("/delete" , methods=['POST' , 'GET'])
def delete():
    idField = request.form["songID"]
    #idField = request.form.get("songID")
    cursor.execute("DELETE FROM songs WHERE songID=" + idField)
    conn.commit()
    songs=readSongs.read()


    return render_template("list.html", deleteMessage=f"Record {idField} deleted from Songs Table", read_songs=songs)
if __name__ == "__main__":
    flask_app.run(debug=True)
