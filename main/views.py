from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
from django.contrib import messages
from django.contrib.auth.models import User
from main.models import Resume, Rating, Skill, Education, PreviousJob, Company
from main.forms import ResumeForm, SkillForm, EducationForm, PreviousJobForm

def landing_page(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        resumes = Resume.objects.filter(
            Q(owner__username__icontains=query) |
            Q(owner__first_name__icontains=query) |
            Q(owner__last_name__icontains=query) |
            Q(previous_jobs__company__name__icontains=query) |
            Q(skills__name__icontains=query) |
            Q(education__school_name__icontains=query)
        ).distinct().annotate(average_rating=Avg('ratings__score'))
        
        return render(request, 'main/landing.html', {
            'resumes': resumes,
            'query': query,
            'is_search': True
        })

    # Rows (8 items per row = 2 rows if 4 items per row in UI)
    top_rated = Resume.objects.annotate(avg_rating=Avg('ratings__score')).filter(avg_rating__isnull=False).order_by('-avg_rating')[:8]
    unrated = Resume.objects.annotate(avg_rating=Avg('ratings__score')).filter(avg_rating__isnull=True)[:8]
    recent = Resume.objects.order_by('-created_at')[:8]
    updated = Resume.objects.order_by('-updated_at')[:8]

    return render(request, 'main/landing.html', {
        'top_rated': top_rated,
        'unrated': unrated,
        'recent': recent,
        'updated': updated,
        'is_search': False
    })

def resume_list(request):
    resumes = Resume.objects.annotate(average_rating=Avg('ratings__score'))
    return render(request, 'main/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    ratings = resume.ratings.all()
    average_rating = ratings.aggregate(Avg('score'))['score__avg']
    return render(request, 'main/resume_detail.html', {
        'resume': resume,
        'ratings': ratings,
        'average_rating': average_rating
    })

@login_required
def edit_resume(request):
    resume, created = Resume.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, "Resume updated successfully.")
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm(instance=resume)
    
    return render(request, 'main/edit_resume.html', {
        'form': form,
        'resume': resume,
        'skills': resume.skills.all(),
        'education': resume.education.all(),
        'previous_jobs': resume.previous_jobs.all(),
        'companies': Company.objects.all()
    })

@login_required
def rate_resume(request, pk):
    if request.method == 'POST':
        resume = get_object_or_404(Resume, pk=pk)
        if resume.owner == request.user:
            messages.error(request, "You cannot rate your own resume.")
            return redirect('resume_detail', pk=pk)
        
        score = request.POST.get('score')
        Rating.objects.update_or_create(
            rater=request.user,
            resume=resume,
            defaults={'score': score}
        )
        messages.success(request, "Rating submitted successfully.")
    return redirect('resume_detail', pk=pk)

# Views for adding child objects
@login_required
def add_skill(request):
    resume, _ = Resume.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.resume = resume
            skill.save()
            return redirect('edit_resume')
    return redirect('edit_resume')

@login_required
def add_education(request):
    resume, _ = Resume.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.resume = resume
            edu.save()
            return redirect('edit_resume')
    return redirect('edit_resume')

@login_required
def add_job(request):
    resume, _ = Resume.objects.get_or_create(owner=request.user)
    if request.method == 'POST':
        form = PreviousJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.resume = resume
            job.save()
            return redirect('edit_resume')
    return redirect('edit_resume')