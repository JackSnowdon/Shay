from django.urls import include, path
from .views import *
from accounts import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
    path('admin_panel/', admin_panel, name="admin_panel"),
    path('password-reset/', include(url_reset)),
    path(r'change_staff_access/<int:pk>', change_staff_access, name="change_staff_access"),
]