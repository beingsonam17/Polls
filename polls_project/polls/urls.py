from django.urls import path
from . import views


# TEMPLATE URLS!!
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    

    path('create/',views.QuestionsCreateView.as_view(),name='create'),
    path('createChoice/',views.ChoiceCreateView.as_view(),name='createChoice'),
    path('createChoice/',views.DetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.QuestionsUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.QuestionsDeleteView.as_view(),name='delete'),    
]