from django.conf.urls import url
from core import relay_views, stripe_views


urlpatterns = [
    url(r"^add-stripe/", relay_views.AddStripe.as_view()),
    url(r"^flush-stripes/", relay_views.FlushStripes.as_view()),
    url(r"^set-pixel-color/", relay_views.SetPixelColor.as_view()),
    url(r"^show/", relay_views.Show.as_view()),
    url(r"^set-segment-color/", relay_views.SetSegmentColor.as_view()),
    url(r"^execute-effect/fireplace/", relay_views.ExecuteEffectFireplace.as_view()),
    url(r"^stop-effect/", relay_views.StopEffect.as_view()),
    url(r"^stripes/", relay_views.GetStripes.as_view()),
    url(r"^stripe/(?P<pk>[0-9]+)/", stripe_views.GetStripe.as_view()),
    url(
        r"^stripe/set-pixel-color/(?P<pk>[0-9]+)", stripe_views.SetPixelColor.as_view()
    ),
    url(r"^stripe/show/(?P<pk>[0-9]+)", stripe_views.Show.as_view()),
    url(
        r"^stripe/set-segment-color/(?P<pk>[0-9]+)",
        stripe_views.SetSegmentColor.as_view(),
    ),
]