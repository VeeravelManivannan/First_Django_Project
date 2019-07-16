from django.contrib import admin
from .models import Question,Choice



#For Inline choice model(ie editing both the PARENT and CHILD model in the same admin page)
class ChoiceInLine(admin.TabularInline):
    model = Choice


#Modeladmins
class QuestionAdmin(admin.ModelAdmin):
    fields = ('pub_date','question_text')
    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin)    

#admin.site.register(Choice)
