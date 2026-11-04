from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser


class UpdateProfileTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='student',
            password='test-password-123',
            email='old@example.com',
            first_name='Old',
            course='Old course',
        )

    def test_requires_login(self):
        response = self.client.get(reverse('update-profile'))

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("update-profile")}',
        )

    def test_updates_logged_in_user_profile(self):
        self.client.login(username='student', password='test-password-123')

        response = self.client.post(reverse('update-profile'), {
            'username': 'student-updated',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'Name',
            'course': 'New course',
        }, follow=True)

        self.assertRedirects(response, reverse('dashboard'))
        self.assertContains(response, 'Your profile was updated successfully.')
        self.assertContains(response, 'role="alert"')
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'student-updated')
        self.assertEqual(self.user.email, 'new@example.com')
        self.assertEqual(self.user.first_name, 'New')
        self.assertEqual(self.user.last_name, 'Name')
        self.assertEqual(self.user.course, 'New course')

    def test_role_cannot_be_changed_through_profile_form(self):
        self.client.login(username='student', password='test-password-123')

        self.client.post(reverse('update-profile'), {
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'course': self.user.course,
            'role': CustomUser.Role.ADMIN,
        })

        self.user.refresh_from_db()
        self.assertEqual(self.user.role, CustomUser.Role.STUDENT)
