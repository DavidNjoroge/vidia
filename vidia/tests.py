from django.test import TestCase
from .models import Project
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        # self.james = User(username='davy',password='boomshakalaka')
        # self.james.save()
        self.game = Project(title='dsfgff',description='dfsfasd',github_link='sdfsdfsdf',deployed_link='sdfdafgdfs',picture='sdfsfsdf')
        # self.game.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.game,Project))

    