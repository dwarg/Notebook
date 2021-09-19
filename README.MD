## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#how-to-use)  
* [Setup](#setup)         

## General info
It's a notebook project based on Flask and API with full support of CRUD methods.

## Technologies
Project is created with:
* Python
* SQLAlchemy
* SQLite

## How to use
* [GET] /api/note - for list of all notes in database
* [GET] /api/note/<id> - for detail note
* [POST] /api/note - for add note to database
* [POST] /api/note/add_note - for generate sample notes to database
* [PUT] /api/note/<id> - for update specified note
* [DELETE] /api/note/<id> - for delete specified note

## Setup
```
$ git clone https://github.com/Dwarg/Notebook-Flask.git
$ cd Notebook-Flask
$ pip install -r requirements.txt
$ flask run
```
