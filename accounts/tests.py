# yourapp/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
# from accounts.models import UserAccountManager  

class UserAccountManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        manager = User.objects

        email = "test@example.com"
        password = "testpassword"
        first_name = "John"
        last_name = "Doe"

        user = manager.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        manager = User.objects

        email = "admin@example.com"
        password = "adminpassword"
        first_name = "Admin"
        last_name = "User"

        superuser = manager.create_superuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertEqual(superuser.first_name, first_name)
        self.assertEqual(superuser.last_name, last_name)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class UserAccountTests(TestCase):

    def test_user_str_method(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
            first_name="John",
            last_name="Doe"
        )

        self.assertEqual(str(user), user.email)
