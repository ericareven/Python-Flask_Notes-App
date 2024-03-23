function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/"
    })
}

function deleteJournal(journalId) {
    fetch('/delete-journal', {
        method: 'POST',
        body: JSON.stringify({ journalId: journalId }),
    }).then((_res) => {
        window.location.href = "/journal"
    })
}