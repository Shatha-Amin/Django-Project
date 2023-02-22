
# Register your models here.
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import StudentProfile, TeacherProfile

class UserProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False

class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, TeacherProfileInline)

    def save_model(self, request, obj, form, change):
        # generate a random password for the user
        password = User.objects.make_random_password()
        obj.set_password(password)

        # save the user and profile
        obj.save()
        profile = None
        if 'studentprofile' in form.cleaned_data:
            # create a student profile
            profile = obj.studentprofile
            profile.name = obj.username
            profile.email = obj.email
        elif 'teacherprofile' in form.cleaned_data:
            # create a teacher profile
            profile = obj.teacherprofile
            profile.name = obj.username
            profile.email = obj.email

        if profile:
            profile.save()

            # generate a PDF with the login information
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="login_info.pdf"'
            p = canvas.Canvas(response)
            p.drawString(100, 750, f"Username: {obj.username}")
            p.drawString(100, 700, f"Password: {password}")
            p.showPage()
            p.save()
            return response

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)