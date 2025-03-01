from django.urls import path
from DefectsPortal import views

urlpatterns = [
    path('', views.alldefects,name='defects'),
    path('descr/<int:id>',views.Defects_description,name='descr'),
    path('add_defects',views.add_defect,name='add_defects'),
    path('edit/<int:id>',views.update_defects,name='edit'),
    path('delete/<int:id>',views.delete_defects,name='delete'),
]
