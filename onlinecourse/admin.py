from django.contrib import admin
# <HINT> Import any new Models here
from .models import Question, Choice
from .models import Course, Lesson, Instructor, Learner

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInLine(admin.StackedInLine):
    model = Question
    extra = 2
class ChoiceInLine(admin.StackedInLine):
    model = Choice
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
