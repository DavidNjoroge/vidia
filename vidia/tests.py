from django.test import TestCase
from .models import Project
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        self.james = User(username='davy',password='boomshakalaka')
        self.james.save()
        self.game = Project(user=self.james,title='dsfgff',description='dfsfasd',github_link='sdfsdfsdf',deployed_link='sdfdafgdfs',picture='sdfsfsdf')

    def test_instance(self):
        self.assertTrue(isinstance(self.game,Project))

    def test_save_method(self):
        self.game.save_project()
        
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)