#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, request, render_template


app = Flask(__name__)

# from gmail_api import *

#Création de la route et de la fonction liée à celle-ci
@app.route('/', methods=["POST", "GET"])
def Register():
    #On vérifie si la requête utilisée est "POST" 
    if request.method == "POST":
        #Récupération des informations du form envoyer grâce à la requête "POST"
        #Chaque chaine donnée dans le request.form représente le nom des variables donnée dans le fichier html correspondant
        username = request.form["username"]
        adresse = request.form["adresse"]
        mdp = request.form["mdp"]
        Cmdp = request.form["Cmdp"]
        print(username)
        print(adresse)
        print(mdp)
        print(Cmdp)
    #On retourne render_template avec le fichier html qu'on veut utiliser
    return render_template("index.html")

#On fait le main pour run l'app
if __name__ == '__main__':
    app.run()
