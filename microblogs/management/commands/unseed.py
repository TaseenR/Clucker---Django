from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
    def handle(self, *args, **options):
        self.all_users= User.objects.all()
        for each_user in self.all_users:
            if each_user.is_superuser == False:
                each_user.delete()