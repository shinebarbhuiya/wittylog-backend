from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import Entry, EntryEmbedding

class EntryModelTest(TestCase):
    def setUp(self):
        # Create a test user and a token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_entry_creation(self):
        entry = Entry.objects.create(title='Test Title', content='Test Content', author=self.user)
        self.assertEqual(str(entry), 'Test Title')
        self.assertIsNotNone(entry.id)
        self.assertIsNotNone(entry.created_at)
        self.assertIsNotNone(entry.updated_at)

    def test_entry_embedding_creation(self):
        entry = Entry.objects.create(title='Test Title', content='Test Content', author=self.user)
        embedding = EntryEmbedding.objects.create(entry=entry, embedding=[1.0, 2.0, 3.0], text='Test Text')
        self.assertEqual(str(embedding), str(entry))
        self.assertIsNotNone(embedding.id)

    def test_entry_save_with_request(self):
        entry_count_before = Entry.objects.count()

        # Simulate a request with authentication token
        request = self.client.get('/fake-url/', HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create a new entry using the simulated request
        Entry.objects.create(title='Test Title', content='Test Content', request=request)

        entry_count_after = Entry.objects.count()
        self.assertEqual(entry_count_after, entry_count_before + 1)

    # Add more test cases as needed

class EntryEmbeddingModelTest(TestCase):
    def test_entry_embedding_creation(self):
        entry = Entry.objects.create(title='Test Title', content='Test Content', author=User.objects.create_user(username='testuser', password='testpassword'))
        embedding = EntryEmbedding.objects.create(entry=entry, embedding=[1.0, 2.0, 3.0], text='Test Text')
        self.assertEqual(str(embedding), str(entry))
        self.assertIsNotNone(embedding.id)

    # Add more test cases as needed
