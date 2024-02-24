from core.admin import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('login/', LoginView.as_view(template_name="users/sign_in.html",success_url="/"), name='login'),
    path('logout.html/', LogoutView.as_view(template_name="users/logout.html.html",success_url="/"), name='logout.html'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
