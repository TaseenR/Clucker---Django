from django.contrib.auth.hashers import check_password
from django.http import response
from django.test import TestCase
from microblogs.forms import SignUpForm
from microblogs.models import User
from django.urls import reverse

class SignUpViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'username': '@janedoe',
        'email': 'janedoe@example.org',
        'bio': 'My bio',
        'new_password': 'Password123',
        'password_confirmation': 'Password123'
        }

    def test_sign_up_url(self):
        self.assertEqual(self.url,'/sign_up/')
        
    def test_unsuccesful_sign_up(self):
        self.form_input['username'] = "BadName"
        before_count = User.objects.count()
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signUp.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)


    def test_get_successful_sign_up(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input, follow= True)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        response_url = reverse('feed')
        self.assertRedirects(response, response_url,status_code=302,target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
        user = User.objects.get(username= '@janedoe')
        self.assertTrue(check_password('Password123', user.password))