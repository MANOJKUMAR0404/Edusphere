from django.urls import path
from . import views
urlpatterns = [
    # Teachers
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login',views.Teacher_login),

    # teacher dashboard
    path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),

    # category
    path('category/',views.CategoryList.as_view()),

    # course
    path('course/',views.CourseList.as_view()),

    path('course/<int:pk>/',views.CourseDetailView.as_view()),

    # teacher-course
    path('teacher-courses/<int:teacher_id>',views.TeacherCourseList.as_view()),

    # specific course detail
    path('teacher-course-detail/<int:pk>',views.TeacherCourseDetail.as_view()),

    # specific course chapters
    path('course-chapters/<int:course_id>',views.CourseChapterList.as_view()),

    # teacher-chapter
    path('chapter/',views.ChapterList.as_view()),

    path('chapter/<int:pk>',views.ChapterDetailView.as_view()),

    # student register
    path('student/', views.StudentList.as_view()),

    # student login
    path('student-login',views.Student_login),

    # student enroll course
    path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),

    path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),

    path('fetch-enrolled-students/<int:course_id>',views.EnrolledStudents.as_view()),

    path('fetch-recommended-courses/<int:studentId>',views.CourseList.as_view()),

    path('fetchall-enrolled-students/<int:teacher_id>',views.EnrolledStudents.as_view()),

    path('course-rating/', views.CourseRatingList.as_view()),

    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),
]