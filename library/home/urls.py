from django.urls import path, include

app_name = 'home'
urlpatterns = [
    path('', include('rest_framework.urls'))
]