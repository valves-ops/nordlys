from django.conf.urls import url
from core import views


urlpatterns = [
    url(r"^add-stripe/", views.AddStripe.as_view()),
    url(r"^set-pixel-color/", views.SetPixelColor.as_view()),
    url(r"show/", views.Show.as_view()),
    url(r"set-segment-color/", views.SetSegmentColor.as_view()),
]