# Create your tests here.
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Resume, PreviousJob, Education, Skill, Company
from django.contrib.auth.models import User
# Create your tests here.
class ResumeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create test data
        self.owner = User.objects.create_user(
            username='john', 
            password='password', 
            email='john.doe@gmail.com',
            first_name='John',
            last_name='Doe'
        )

        self.resume = Resume.objects.create(
            owner=self.owner,
            success_summary="Experienced software engineer with 5+ years of experience.",
        )
        
        self.company = Company.objects.create(
            name="Tech Corp",
            location="New York",
            description="Leading technology company"
        )
        self.job = PreviousJob.objects.create(
            resume=self.resume,
            company=self.company,
            position="Software Engineer",
            start_date="2018-01-01",
            end_date="2022-12-31",
            description="Developed web applications using Python and Django."
        )
        
        self.education = Education.objects.create(
            resume=self.resume,
            school_name="University of Technology",
            degree="Bachelor of Science",
            start_date="2017-05-01",
            end_date="2022-12-31"
        )
        
        self.skill = Skill.objects.create(
            resume=self.resume,
            name="Python",
        )
        

    def test_list_resumes(self):
        response = self.client.get('/resumes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['owner'], self.owner.id)

    def test_retrieve_resume(self):
        response = self.client.get(f'/resumes/{self.resume.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['owner'], self.owner.id)

    def test_create_skill(self):
        data = {
            'resume': self.resume.id,
            'name': 'Django',
        }
        self.client.force_authenticate(user=self.owner)
        response = self.client.post('/skills/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Skill.objects.count(), 2)
        self.assertEqual(response.data['resume'], self.resume.id)

    def test_update_skill(self):
        data = {
            'resume': self.resume.id,
            'name': 'New Skill'
        }
        response = self.client.put(f'/skills/{self.skill.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['resume'], self.resume.id)

    def test_delete_resume(self):
        response = self.client.delete(f'/resumes/{self.resume.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Resume.objects.count(), 0)

    def test_list_previous_jobs(self):
        response = self.client.get('/previous-jobs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['company'], self.company.id)

    def test_list_educations(self):
        response = self.client.get('/educations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['school_name'], 'University of Technology')

    def test_list_skills(self):
        response = self.client.get('/skills/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Python')
