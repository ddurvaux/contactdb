from contactdb import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


router = DefaultRouter()
router.register(r'countrycodes', views.CountrycodeViewSet)
router.register(r'sources', views.SourceViewSet)
router.register(r'organisations', views.OrganisationViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'asns', views.ASNViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^pgpkeys/(?P<fingerprint>[a-zA-Z0-9]+)$', views.PGPKey),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^admin/', include(admin.site.urls)),
)
