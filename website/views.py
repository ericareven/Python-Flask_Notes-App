from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Journal, DailyPrompt, Mood
from datetime import datetime, timedelta
from .prompts import daily_prompts
from .quotes import quotes
from . import db
import json
import random

views = Blueprint('views', __name__)

# Home
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    random_quote = random.choice(quotes)
    
    return render_template("home.html", user=current_user, random_quote=random_quote)

# Mood Tracker
@views.route('/mood', methods=['GET', 'POST'])
@login_required
def moodTracker():
    # Calculate the start and end dates for the desired time period (e.g., current week or month)
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Start of the current week
    end_of_week = start_of_week + timedelta(days=6)           # End of the current week
    start_of_month = today.replace(day=1)                     # Start of the current month
    end_of_month = start_of_month.replace(day=28) + timedelta(days=4) - timedelta(days=start_of_month.day)
    
    # Query mood entries for the desired time period
    mood_entries = Mood.query.filter(Mood.date.between(start_of_week, end_of_week)).all()
    # Or for monthly tracking: Mood.query.filter(Mood.date.between(start_of_month, end_of_month)).all()

    if request.method == 'POST':
        mood = request.form.get('mood')
        if mood:
            new_mood = Mood(mood=mood, user_id=current_user.id)
            db.session.add(new_mood)
            db.session.commit()
            flash('Mood logged successfully!', category='success')
        else:
            flash('Please select a mood.', category='error')

    return render_template("mood.html", user=current_user, mood_entries=mood_entries)
# def moodTracker():
#     if request.method == 'POST':
#         mood = request.form.get('mood')
#         if mood:
#             new_mood = Mood(mood=mood, user_id=current_user.id)
#             db.session.add(new_mood)
#             db.session.commit()
#             flash('Mood logged successfully!', category='success')
#         else:
#             flash('Please select a mood.', category='error')

#     return render_template("mood.html", user=current_user)

# Notes
@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
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

    return render_template("notes.html", user=current_user)


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
    # Get the last used prompt
    daily_prompt = DailyPrompt.query.first()
    # If no prompt exists or the last used date is not today, generate a new prompt
    if not daily_prompt or daily_prompt.last_used_date != datetime.today().date():
        prompt_text = random.choice(daily_prompts)
        
        # Update or create a new DailyPrompt record
        if not daily_prompt:
            daily_prompt = DailyPrompt(prompt=prompt_text, last_used_date=datetime.today().date())
            db.session.add(daily_prompt)
        else:
            daily_prompt.prompt = prompt_text
            daily_prompt.last_used_date = datetime.today().date()
        db.session.commit()

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

    return render_template("journal.html", user=current_user, daily_prompt=daily_prompt.prompt)


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