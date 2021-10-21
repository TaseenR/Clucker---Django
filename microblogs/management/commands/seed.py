from re import S
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args,**options):
        print("Warning seed has not been implemented")
        for _ in range(100):
            self.user = User.objects.create_user(
                username = '@'+self.faker.unique.user_name(),
                first_name= self.faker.first_name(),
                last_name= self.faker.last_name(),
                email=self.faker.unique.free_email(),
                password= self.faker.password(),
                bio = self.faker.text())
            print(self.user.first_name +" "+self.user.email)