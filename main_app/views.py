# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse
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
    
class Idea:
    def __init__(self, name, img, company, details, difficulty):
        self.name = name
        self.img = img
        self.company = company
        self.details = details
        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if isinstance(difficulty, DifficultyLevel):
            self.difficulty = difficulty
        else:
            raise ValueError("Difficulty must be an instance of DifficultyLevel Enum")

# Example usage
ideas = [
    Idea('nothing', 'main_app/static/images/logo.png', 'microsoft','its good!',DifficultyLevel.EIGHT)
]

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ideas_index(request):
    return render(request, 'ideas/index.html', {'ideas':ideas})





