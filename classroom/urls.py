from django import views
from django.urls import path
from .views.room import ViewClassRoom,SingleClass,CreateClassRoom,JoinRoom, LeaveClass, SendMail
from .views.people import PeopleUnderRoom
from .views.stream import CreateStream, CreateComment
from .views.assignment import ExamView,AssignmentCreateView,AssignmentView,AssignmentDeleteView,ExamCreateView,ExamListView,AssignmentSubmissionView,ExamDeleteView,ExamSubmissionView,ExamSubmissionListView,AssignmentSubmissionListView,AssignmentSubmissionDelete,ExamSubmissionDelete
urlpatterns =[
    path('',ViewClassRoom.as_view(),name='all_class'),
    path('view/<str:id>/',SingleClass.as_view(), name='single'),
    path('create/',CreateClassRoom.as_view(),name='create_class'),
    path('join/class/',JoinRoom.as_view(),name='join'),
    path('<str:id>/people/', PeopleUnderRoom.as_view(),name='people'),
    path('<str:id>/leave/', LeaveClass.as_view(), name='leave'),
    path('<str:id>/create/stream',CreateStream.as_view(),name='stream_create'),
    path('<str:id>/create/comment', CreateComment.as_view(),name='comment_create'),
    #send email route
    path('send/code/via/mail',SendMail.as_view(),name='send'),
    path('exam/', ExamView.as_view(), name='exam'),
    path('assignment-create/', AssignmentCreateView.as_view(), name='assignment-create'),
    path('assignment/', AssignmentView.as_view(), name='assignment-list'),
    path('<pk>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),
    path('exam-create/', ExamCreateView.as_view(), name='exam-create'),
    path('exam-list/', ExamListView.as_view(), name='exam-list'),
    path('<pk>/delete/', ExamDeleteView.as_view(), name='delete-exam'),
    path('assignment-submission/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
    path('exam-submission/', ExamSubmissionView.as_view(), name='exam-submission'),
    path('exam-submission-list/', ExamSubmissionListView.as_view(), name='exam-submission-list'),
    path('assignment-submission-list/', AssignmentSubmissionListView.as_view(), name='assignment-submission-list'),
    path('<pk>/delete/', AssignmentSubmissionDelete.as_view(), name='assignment-submission-delete'),
    path('<pk>/delete/', ExamSubmissionDelete.as_view(), name='exam-submission-delete'),
]