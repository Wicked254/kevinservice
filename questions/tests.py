from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username='GEORGE', email='geojeff@example.com', password='password')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'GEORGE')
        self.assertEqual(user.email, 'geojeff@example.com')
        self.assertTrue(user.check_password('password'))
