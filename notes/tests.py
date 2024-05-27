from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note
from django.contrib.messages import get_messages

class NoteModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_note(self):
        note = Note.objects.create(
            title='Test Note',
            content='This is a test note.',
            user=self.user
        )
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note.')
        self.assertEqual(note.user.username, 'testuser')

class NoteViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.',
            user=self.user
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)  # Redirection after creation
        self.assertEqual(Note.objects.last().title, 'New Note')
        
        # Test notification message
        response = self.client.get(reverse('note_list'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Note created successfully.')

    def test_note_update_view(self):
        response = self.client.post(reverse('note_update', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'This is an updated note.'
        })
        self.assertEqual(response.status_code, 302)  # Redirection after update
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        
        # Test notification message
        response = self.client.get(reverse('note_list'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Note updated successfully.')

    def test_note_delete_view(self):
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirection after deletion
        self.assertEqual(Note.objects.count(), 0)
        
        # Test notification message
        response = self.client.get(reverse('note_list'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Note deleted successfully.')

    def test_search_notes_view(self):
        response = self.client.get(reverse('search_notes') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_list_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_note_create_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_note_detail_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_note_update_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('note_update', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_note_delete_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
