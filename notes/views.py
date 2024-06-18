from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# View for the index page
def index(request):
    """Render the index page."""
    return render(request, 'index.html')


# View for user registration
def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# View to list all notes for the logged-in user
@login_required
def note_list(request):
    """Display a list of notes for the logged-in user."""
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


# View to display the details of a specific note
@login_required
def note_detail(request, id):
    """Display the details of a specific note."""
    note = get_object_or_404(Note, id=id, user=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})


# View to create a new note
@login_required
def note_create(request):
    """Create a new note."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note created successfully.')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


# View to update an existing note
@login_required
def note_update(request, id):
    """Update an existing note."""
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully.')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


# View to delete an existing note
@login_required
def note_delete(request, id):
    """Delete an existing note."""
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully.')
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


# View to search for notes
@login_required
def search_notes(request):
    """Search for notes by title or content."""
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Note.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            user=request.user
        )
    return render(request, 'notes/search_results.html', {'results': results, 'query': query})