from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
work_choices = (
    ('freelance', 'Freelancer'),
    ('company', 'Company'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=140, blank=True)
    phone_number = PhoneNumberField()
    country = models.CharField(max_length=140, blank=True)
    url = models.CharField(max_length=250, blank=True)
    work = models.CharField(max_length=30, choices=work_choices)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)


class Tag(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tag')
    category = models.CharField(max_length=50)

    def save_tag(self):
        self.save()

    @classmethod
    def display_tags(cls):
        tags = cls.objects.all()
        return tags

    @classmethod
    def get_single_tag(cls, pk):
        tag = cls.objects.get(pk=pk)
        return tag

    def __str__(self):
        return self.category


class Project(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    picture = models.ImageField(upload_to='project_pics')
    github_link = models.CharField(max_length=250)
    deployed_link = models.CharField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True)

    # manytomany relationship
    tags = models.ManyToManyField(
        Tag, related_name='tag')

    class Meta:
        ordering = ['-post_date']

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def save_project(self):
        self.save()

    @classmethod
    def display_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_single_project(cls, pk):
        project = cls.objects.get(pk=pk)
        return project

    @classmethod
    def display_users_projects(cls, id):
        projects = cls.objects.filter(user_id=id)
        return projects

    def __str__(self):
        return self.title

# class Rating(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     project=models.ForeignKey(Project,on_delete=models.CASCADE)
#     content=models.IntegerField()
#     usability=models.IntegerField()
#     design=models.IntegerField()