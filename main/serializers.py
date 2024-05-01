from rest_framework import serializers
from . import models
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id','full_name','detail','email','password','qualification','profile_photo','mobile','skills','teacher_courses','skill_list']
    def __init__(self,*args,**kwargs):
        super(TeacherSerializers,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=1

class TeacherDashboardSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_courses','total_teacher_chapters','total_teacher_students']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Coursecategory
        fields=['id','title','description']

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields=['id','category','teacher','title','description','featured_image','techs','course_chapters','related_videos','tech_list','total_enrolled_students','course_rating']

    def __init__(self,*args,**kwargs):
         super(CourseSerializers,self).__init__(*args,**kwargs)
         request=self.context.get('request')
         self.Meta.depth=0
         if request and request.method == 'GET':
             self.Meta.depth=1
        
class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Chapter
        fields=['id','course','title','description','video','remarks']

    def __init__(self,*args,**kwargs):
        super(ChapterSerializers,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=1

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=['id','full_name','email','password','qualification','mobile','address','interest_field']
        
    def __init__(self,*args,**kwargs):
        super(StudentSerializers,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=1

class StudentEnrollCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.StudentCourseEnrollment
        fields=['id','course','student','enrolled_time']
        
    def __init__(self,*args,**kwargs):
        super(StudentEnrollCourseSerializers,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=1


class CourseRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.CourseRating
        fields=['id','course','student','rating','reviews','review_time']
        
    def __init__(self,*args,**kwargs):
        super(CourseRatingSerializers,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=1