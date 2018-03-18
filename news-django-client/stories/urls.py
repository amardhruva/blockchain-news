from django.conf import settings
from django.urls import path


from stories.views import HomePageView, AddNewsView, ImageView, ShowNewsView, AddUserView
from django.conf.urls.static import static

app_name = 'stories'

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('addnews/', AddNewsView.as_view(), name="addnews"),
    path('shownews/<int:newsid>/', ShowNewsView.as_view(), name="shownews"),
    path('image/<slug:hash>/', ImageView.as_view(), name="image"),
    path('adduser/', AddUserView.as_view(), name="adduser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)