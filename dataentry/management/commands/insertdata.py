from django.core.management.base import BaseCommand
from dataentry.models import Student

#i want to add some data to the database using custom command

class Command(BaseCommand):
    help = "insert data to the database"
    
    def handle(self,*args,**kwargs):
        #logic goes here
        #add one data
        dataset = [
            {'roll_no':102,'name':'biren','age':29},
            {'roll_no':103,'name':'gopal','age':30},
            {'roll_no':104,'name':'mehmud','age':31},
        ]
        
        for data in dataset:
            Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
        self.stdout.write(self.style.SUCCESS('data insert successfully'))