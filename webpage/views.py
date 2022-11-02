from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'webpage/index.html')


def profile_view(request):
    context = {'firstname': 'Sadegh', 'lastname': 'Mehdizadeh', 'age': '37', 'city': 'Tehran', 'country': 'Iran', 'job1': 'freelancer', 'job2': 'learner', 'job3': 'teacher',
               'interest1': 'python', 'interest2': 'database and SQL Server', 'interest3': 'Bash Scripting', 'interest4': 'machine learning', 'interest5': 'backend programming', 'number': 'No.1', 'street': 'Azadi street', 'email': 'sdg.mhz@gmail.com', 'phone': '+98-912-345-6789', 'site': 'www.sdgmhz.com'}
    return render(request, 'webpage/profile.html', context)


def education_view(request):
    context = {'Bsc': 'Mechanical Engieering in Farm Machinery', 'Bsc_year': '2008', 'Bsc_Univ': 'Isfahan University of Technology', 'Bsc_Thesis': 'Optimization in Corn Harvesting Machine',
               'Msc': 'Mechatronics Engineering', 'Msc_year': '2012', 'Msc_Univ': 'University of Semnan', 'Msc_Thesis': 'Object Detection in Video Images Using Neural-Fuzzy Network'}
    return render(request, 'webpage/education.html', context)


def languages_view(request):
    context = {'lan1': 'ENGLISH', 'level1': 'FLUENT', 'lan2': 'FRENCH',
               'level2': 'BASIC FAMILARITY', 'lan3': 'RUSSIAN', 'level3': 'BASIC FAMILARITY'}
    return render(request, 'webpage/languages.html', context)


def projects_view(request):
    context = {'pr1': 'Live video stream object recognition using Open-CV', 'pr2': 'Develop a machine learning system in car price prediction based on web scraping',
               'pr3': 'Heart attack prediction system based on classification', 'pr4': 'Different clustering projects'}
    return render(request, 'webpage/projects.html', context)


def skills_view(request):
    context = {'sk1': 'Step-7 PLC Programming', 'sk1p': '70%', 'sk2': 'Python', 'sk2p': '70%', 'sk3': 'machine learning',
               'sk3p': '50%', 'sk4': 'linux bash scripting', 'sk4p': '50%', 'sk5': 'html5+css3', 'sk5p': '40%', 'sk6': 'git', 'sk6p': '80%'}
    return render(request, 'webpage/skills.html', context)


def contact_view(request):
    context = {'address': 'No.1 Azadi Street, Tehran, Iran',
               'phone': '+98-912-345-6789'}
    return render(request, 'webpage/contact.html', context)
