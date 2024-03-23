from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Journal
from . import db
import json

views = Blueprint('views', __name__)

# Notes
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note') #Gets the note from the HTML 

        if len(note) < 1:
        # if not note:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

# Journal
@views.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST': 
        journal = request.form.get('journal') #Gets the journal entry from the HTML 

        if len(journal) < 1:
        # if not journal:
            flash('Journal entry is too short!', category='error') 
        else:
            new_journal = Journal(data=journal, user_id=current_user.id)  #providing the schema for the journal entry 
            db.session.add(new_journal) #adding the journal entry to the database 
            db.session.commit()
            flash('Journal entry added!', category='success')

    return render_template("journal.html", user=current_user)


@views.route('/delete-journal', methods=['POST'])
def delete_journal():  
    journal = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    journalId = journal['journalId']
    journal = Journal.query.get(journalId)
    if journal:
        if journal.user_id == current_user.id:
            db.session.delete(journal)
            db.session.commit()

    return jsonify({})