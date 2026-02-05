import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Resume, Skill, Education, PreviousJob, Company, Rating
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake Resumes with various details'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=3000,
            help='Number of resumes to generate'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing resumes and related data before generating'
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options['number']
        clear = options['clear']

        if clear:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            Rating.objects.all().delete()
            PreviousJob.objects.all().delete()
            Education.objects.all().delete()
            Skill.objects.all().delete()
            Resume.objects.all().delete()
            User.objects.filter(is_staff=False, is_superuser=False).delete()
            Company.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Data cleared.'))

        self.stdout.write(f'Generating {count} resumes...')

        # Ensure some companies exist
        if not Company.objects.exists():
            for _ in range(20):
                Company.objects.create(
                    name=fake.company(),
                    location=fake.city(),
                    description=fake.catch_phrase()
                )
        
        companies = list(Company.objects.all())
        
        # Predefined skills for variety
        skill_pool = [
            "Python", "Django", "JavaScript", "React", "Vue", "SQL", "PostgreSQL",
            "Docker", "Kubernetes", "AWS", "Azure", "GCP", "HTML", "CSS",
            "Machine Learning", "Data Analysis", "Project Management", "Agile",
            "Scrum", "Java", "C++", "C#", "Go", "Rust", "Swift", "Kotlin"
        ]

        degrees = [
            "B.S. in Computer Science", "M.S. in Data Science", 
            "B.A. in Business Administration", "MBA",
            "B.E. in Software Engineering", "Ph.D. in Artificial Intelligence",
            "B.Sc. in Information Technology"
        ]

        users = []
        for i in range(count):
            username = f"user_{fake.unique.user_name()}_{i}"
            user = User.objects.create_user(
                username=username,
                email=fake.email(),
                password='password123'
            )
            users.append(user)

            resume = Resume.objects.create(
                owner=user,
                success_summary=fake.paragraph(nb_sentences=5)
            )

            # Add Skills
            num_skills = random.randint(3, 8)
            chosen_skills = random.sample(skill_pool, num_skills)
            for skill_name in chosen_skills:
                Skill.objects.create(resume=resume, name=skill_name)

            # Add Education
            num_edu = random.randint(1, 2)
            for _ in range(num_edu):
                Education.objects.create(
                    resume=resume,
                    school_name=fake.company() + " University",
                    degree=random.choice(degrees),
                    start_date=fake.date_between(start_date='-10y', end_date='-4y'),
                    end_date=fake.date_between(start_date='-4y', end_date='today'),
                    description=fake.sentence()
                )

            # Add Previous Jobs
            num_jobs = random.randint(1, 4)
            for _ in range(num_jobs):
                PreviousJob.objects.create(
                    resume=resume,
                    company=random.choice(companies),
                    position=fake.job(),
                    start_date=fake.date_between(start_date='-5y', end_date='-1y'),
                    end_date=fake.date_between(start_date='-1y', end_date='today'),
                    description=fake.paragraph(nb_sentences=3)
                )

        # Generate Ratings
        self.stdout.write('Generating ratings...')
        for user in random.sample(users, min(len(users), 500)):
            # Each sampled user rates 1-5 random resumes
            num_ratings = random.randint(1, 5)
            target_resumes = Resume.objects.order_by('?')[:num_ratings]
            for resume in target_resumes:
                if user != resume.owner:
                    Rating.objects.get_or_create(
                        rater=user,
                        resume=resume,
                        defaults={'score': random.randint(1, 5)}
                    )

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} resumes.'))
