from django.urls import path
from . import views

urlpatterns = [
    path('',views.course_list,name="courses"),
    path('<slug:category_slug>/<int:course_id>',views.course_detail,name="course_detail"),
    path('categories/<slug:category_slug>/',views.category_list,name="category_list"),
    path('tags/<slug:tag_slug>',views.tag_list,name="tag_list"),
    path('search/',views.search,name="search"),







]
