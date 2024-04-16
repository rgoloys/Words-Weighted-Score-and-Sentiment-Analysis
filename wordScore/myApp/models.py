from django.db import models
from django.contrib.auth.models import User
import random
from django.contrib.auth import get_user_model
from django.utils import timezone
class KeyWord(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keywords = models.CharField(max_length=100)
    score = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    admin_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)
    color_code = models.CharField(max_length=7, default='#000000')  # Field to store color code

    def __str__(self):
        return self.keywords

    def save(self, *args, **kwargs):
        if not self.color_code or self.color_code == '#000000':  # Generate random color code if not provided or default
            self.color_code = '#{0:06x}'.format(random.randint(0, 0xffffff))
        if self.score is None:  # Generate random score if not provided
            self.score = random.randint(1, 100)
        super(KeyWord, self).save(*args, **kwargs)


class AcceptScore(models.Model):
    score_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    admin_user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=2)

    def __str__(self):
        return str(self.score_id)

class FileKeywordCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10)
    keyword_count = models.JSONField()
    date_added = models.DateField(default=timezone.now)
    def __str__(self):
        return f"File: {self.file.name}, User: {self.user.username}"

    def calculate_overall_total(self):
        overall_total = 0
        for data in self.keyword_count.values():
            overall_total += data['total']
        return overall_total




class UploadedFile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    document = models.FileField(upload_to='uploads/sentiment/')
    similarity_score = models.FloatField(null=True, blank=True)
    date_added = models.DateField(default=timezone.now)

class AdminInput(models.Model):
    paragraph = models.TextField()
    color = models.CharField(max_length=7, default='#000000')  # Field to store color code

    def __str__(self):
        return self.paragraph
    
    def save(self, *args, **kwargs):
        if not self.color or self.color == '#000000':  # Generate random color code if not provided or default
            self.color = '#{0:06x}'.format(random.randint(0, 0xffffff))
        super(AdminInput, self).save(*args, **kwargs)  # Fix the super call here
