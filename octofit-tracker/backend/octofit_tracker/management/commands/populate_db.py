from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='captain@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=captain, activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=superman, activity_type='Flying', duration=120, date=timezone.now().date())

        # Create Workouts
        workout1 = Workout.objects.create(name='Push Ups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Sprints', description='Speed training')
        workout1.suggested_for.set([ironman, batman])
        workout2.suggested_for.set([captain, superman])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
