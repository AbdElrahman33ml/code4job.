from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
'''
#inheritance from models to access fileds
#fields in django importance
    - html widget
    - validation
    - db size
'''

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)



class job(models.Model):
    owner=models.ForeignKey(User, verbose_name=("Job_owner"), on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    #location
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    job_description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='jobs/')
    slug=models.SlugField(blank=True, null=True)


    def save(self, *args , **kwargs):
        self.slug= slugify(self.title)
        super(job,self).save(*args , **kwargs)

    def __str__(self):
     return self.title


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
     return self.name
    



class Apply (models.Model):
   job=models.ForeignKey("job", verbose_name=("apply"), on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
   email=models.EmailField()
   Portfolio_link=models.URLField()
   cv=models.FileField(upload_to='apply/')
   cover_letter=models.TextField(max_length=500)
   applied_at=models.DateTimeField(auto_now=True)
   
   def __str__(self):
        return self.name