from django.urls import path
from . import views
urlpatterns =[

    # path("tickets/",views.no_model_no__rest),
    path("tickets/",views.Generics_list.as_view()),
    path("tickets/<int:pk>",views.Generics_pk.as_view())

]

