
from django.db import models
from django.urls import reverse
from enum import Enum

class DifficultyLevel(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10

class Idea(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    company = models.CharField(max_length=50)
    details = models.TextField(max_length=500)
    difficulty = models.IntegerField(choices=[(tag.value, tag.name) for tag in DifficultyLevel], default= 1)

    def set_difficulty(self, difficulty):
        if isinstance(difficulty, DifficultyLevel):
            self.difficulty = difficulty.value
        else:
            raise ValueError("Difficulty must be an instance of DifficultyLevel Enum")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('idea-detail', kwargs={'idea_id': self.id})


