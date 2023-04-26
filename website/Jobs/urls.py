from django.urls import path
from . import views

app_name ="jobs"

urlpatterns = [
    path('jobs-list/',views.jobs_list,name = 'jobs_list'),
    path("<int:id>/", views.jobs_detail, name="jobs_detail"),
    path("<int:job_id>/apply/",views.apply_job, name ="apply_job")
]
