from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "print hello world"
    
    def handle(self,*args,**kwargs):
        #we write login to perfom inside this handle function
        self.stdout.write("hello world")