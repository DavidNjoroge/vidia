from django.test import TestCase
from .models import Project,Rating
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

class RatingTestClass(TestCase):
    def setUp(self):
        self.james = User(username='davy',password='boomshakalaka')
        self.james.save()
        self.game = Project(user=self.james,title='dsfgff',description='dfsfasd',github_link='sdfsdfsdf',deployed_link='sdfdafgdfs',picture='sdfsfsdf')
        self.game.save_project()
        self.rating=Rating(user=self.james,project=self.game,usability=10,content=10,design=10)
        self.rating2=Rating(user=self.james,project=self.game,usability=2,content=8,design=4)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.rating,Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        ratings=Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    def test_get_average(self):
        self.rating.save_rating()
        self.rating2.save_rating()
        av_rating=Rating.get_average_rating(self.game.id)
        self.assertEqual(av_rating,[7,6,9])