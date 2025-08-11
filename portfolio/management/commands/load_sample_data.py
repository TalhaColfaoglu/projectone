from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from portfolio.models import About, Education, Experience, Skill, Project

class Command(BaseCommand):
    help = 'Load sample data for the portfolio website'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create About data
        about, created = About.objects.get_or_create(
            name='Talha Colfaoğlu',
            defaults={
                'title': 'Bilgisayar Mühendisliği Öğrencisi',
                'description': 'Boğaziçi Üniversitesi\'nde bilgisayar mühendisliği okuyorum. Yazılım geliştirme ve teknoloji konularında tutkulu bir öğrenciyim. Sürekli kendimi geliştirmeye ve yeni teknolojiler öğrenmeye odaklanıyorum.',
                'email': 'talha@example.com',
                'phone': '+90 555 123 4567',
                'location': 'İstanbul, Türkiye',
                'github': 'https://github.com/talhacolfaoglu',
                'linkedin': 'https://linkedin.com/in/talhacolfaoglu',
                'twitter': 'https://twitter.com/talhacolfaoglu',
            }
        )
        if created:
            self.stdout.write(f'Created About: {about.name}')

        # Create Education data
        education_data = [
            {
                'institution': 'Boğaziçi Üniversitesi',
                'degree': 'Bilgisayar Mühendisliği',
                'field_of_study': 'Bilgisayar Mühendisliği',
                'start_date': date(2022, 9, 1),
                'current': True,
                'description': 'Boğaziçi Üniversitesi\'nde bilgisayar mühendisliği eğitimime devam ediyorum.',
            },
            {
                'institution': 'Bursa Nilüfer Borsa İstanbul Fen Lisesi',
                'degree': 'Lise Diploması',
                'field_of_study': 'Fen Bilimleri',
                'start_date': date(2018, 9, 1),
                'end_date': date(2022, 6, 1),
                'current': False,
                'description': 'Bursa Nilüfer Borsa İstanbul Fen Lisesi\'nden mezun oldum.',
            }
        ]

        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created Education: {education.institution}')

        # Create Skills data
        skills_data = [
            {'name': 'Python', 'category': 'programming', 'proficiency': 8},
            {'name': 'Django', 'category': 'framework', 'proficiency': 7},
            {'name': 'JavaScript', 'category': 'programming', 'proficiency': 6},
            {'name': 'HTML/CSS', 'category': 'programming', 'proficiency': 7},
            {'name': 'Git', 'category': 'tool', 'proficiency': 6},
            {'name': 'SQL', 'category': 'database', 'proficiency': 5},
            {'name': 'React', 'category': 'framework', 'proficiency': 5},
            {'name': 'Problem Çözme', 'category': 'soft', 'proficiency': 8},
            {'name': 'Takım Çalışması', 'category': 'soft', 'proficiency': 7},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created Skill: {skill.name}')

        # Create Projects data
        projects_data = [
            {
                'title': 'Kişisel Website',
                'description': 'Django ile geliştirilmiş modern kişisel website projesi. Responsive tasarım ve modern UI/UX prensipleri kullanılarak oluşturuldu.',
                'technologies': 'Django, Python, HTML, CSS, JavaScript, Bootstrap',
                'github_url': 'https://github.com/talhacolfaoglu/personal-website',
                'featured': True,
            },
            {
                'title': 'Mobil Uygulama',
                'description': 'React Native ile geliştirilmiş mobil uygulama projesi. Kullanıcı dostu arayüz ve performanslı çalışma.',
                'technologies': 'React Native, JavaScript, Node.js, Firebase',
                'github_url': 'https://github.com/talhacolfaoglu/mobile-app',
                'featured': True,
            },
            {
                'title': 'Veri Analizi Projesi',
                'description': 'Python kullanarak geliştirilmiş veri analizi ve görselleştirme projesi. Pandas, NumPy ve Matplotlib kütüphaneleri kullanıldı.',
                'technologies': 'Python, Pandas, NumPy, Matplotlib, Jupyter',
                'github_url': 'https://github.com/talhacolfaoglu/data-analysis',
            },
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created Project: {project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data!')
        )
