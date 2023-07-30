from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("quests",views.viewset_guest),
router.register("movie",views.viewset_movie),
router.register("reservations",views.viewset_reservation)
urlpatterns =[

    # path("tickets/",views.no_model_no__rest),
    # path("tickets/",views.Generics_list.as_view()),
    # path("tickets/<int:pk>",views.Generics_pk.as_view())
    path("tickets/",include(router.urls)),
    path("tickets/search_movie",views.search_movie),
    path("tickets/add_reservation",views.new_reservation)


]

