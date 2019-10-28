from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm, SearchForm



# Create your views here.
def notes_list(request): 
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": notes,
    })

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_detail.html", {"note": note})

def new_note(request):
    if request.method == "POST": 
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_list')
    else: 
        form = NoteForm()    

    return render (request, "notes/new_note.html", {"form": form})

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_detail', pk= note.id)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/notes_edit.html', {
        "note": note,
        "form": form,
    })

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {"notes": notes})
    
def search_notes(request):
    searched_notes = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            notes = Note.objects.all()
            data = request.POST.copy()
            for note in notes:
                if data.get('search_text') in note.title:
                    searched_notes.append(note)
            return render(request, 'notes/search_results.html',
                          {'notes': searched_notes})
    else:
        form = SearchForm()
    return render(request, 'notes/search_notes.html', {'form': form})