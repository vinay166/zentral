from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # Sync
    url(r'^webhook/$', views.WebHookView.as_view(), name='webhook'),

    # Pkg infos
    url(r'^pkg_infos/$', views.PkgInfosView.as_view(), name='pkg_infos'),

    # Catalogs
    url(r'^catalogs/$', views.CatalogsView.as_view(), name='catalogs'),
    url(r'^catalogs/(?P<pk>\d+)/update/$', views.UpdateCatalogView.as_view(), name='update_catalog'),

    # Sub manifests
    url(r'^sub_manifests/$', views.SubManifestsView.as_view(), name='sub_manifests'),
    url(r'^sub_manifests/create/$', views.CreateSubManifestView.as_view(), name='create_sub_manifest'),
    url(r'^sub_manifests/(?P<pk>\d+)/$', views.SubManifestView.as_view(), name='sub_manifest'),
    url(r'^sub_manifests/(?P<pk>\d+)/update/$', views.UpdateSubManifestView.as_view(), name='update_sub_manifest'),
    url(r'^sub_manifests/(?P<pk>\d+)/delete/$', views.DeleteSubManifestView.as_view(), name='delete_sub_manifest'),
    url(r'^sub_manifests/(?P<pk>\d+)/add_pkg_info/$',
        views.SubManifestAddPkgInfoView.as_view(), name='sub_manifest_add_pkg_info'),
    url(r'^sub_manifest_pkg_infos/(?P<pk>\d+)/delete/$',
        views.DeleteSubManifestPkgInfoView.as_view(), name='delete_sub_manifest_pkg_info'),
    url(r'^sub_manifests/(?P<pk>\d+)/add_attachment/$',
        views.SubManifestAddAttachmentView.as_view(), name='sub_manifest_add_attachment'),
    url(r'^sub_manifests/(?P<pk>\d+)/add_script/$',
        views.SubManifestAddScriptView.as_view(), name='sub_manifest_add_script'),
    url(r'^sub_manifests/(?P<sm_pk>\d+)/script/(?P<pk>\d+)/update/$',
        views.SubManifestUpdateScriptView.as_view(), name='sub_manifest_update_script'),
    url(r'^sub_manifests_attachment/(?P<pk>\d+)/delete/$',
        views.DeleteSubManifestAttachmentView.as_view(), name='delete_sub_manifest_attachment'),

    # Manifests
    url(r'^manifests/$', views.ManifestsView.as_view(), name='manifests'),
    url(r'^manifests/create/$', views.CreateManifestView.as_view(), name='create_manifest'),
    url(r'^manifests/(?P<pk>\d+)/$', views.ManifestView.as_view(), name='manifest'),
    url(r'^manifests/(?P<pk>\d+)/enrollment/$',
        views.ManifestEnrollmentView.as_view(), name="manifest_enrollment"),
    url(r'^manifests/(?P<pk>\d+)/enrollment_pkg/$',
        views.ManifestEnrollmentPkgView.as_view(), name='manifest_enrollment_pkg'),
    url(r'^manifests/(?P<pk>\d+)/add_catalog/$',
        views.AddManifestCatalogView.as_view(), name='add_manifest_catalog'),
    url(r'^manifests/(?P<pk>\d+)/delete_catalog/(?P<m2m_pk>\d+)/$',
        views.DeleteManifestCatalogView.as_view(), name='delete_manifest_catalog'),
    url(r'^manifests/(?P<pk>\d+)/add_enrollment_package/$',
        views.AddManifestEnrollmentPackageView.as_view(), name='add_manifest_enrollment_package'),
    url(r'^manifests/(?P<pk>\d+)/update_enrollment_package/(?P<mep_pk>\d+)/$',
        views.UpdateManifestEnrollmentPackageView.as_view(), name='update_manifest_enrollment_package'),
    url(r'^manifests/(?P<pk>\d+)/delete_enrollment_package/(?P<mep_pk>\d+)/$',
        views.DeleteManifestEnrollmentPackageView.as_view(), name='delete_manifest_enrollment_package'),
    url(r'^manifests/(?P<pk>\d+)/add_sub_manifest/$',
        views.AddManifestSubManifestView.as_view(), name='add_manifest_sub_manifest'),
    url(r'^manifests/(?P<pk>\d+)/delete_sub_manifest/(?P<m2m_pk>\d+)/$',
        views.DeleteManifestSubManifestView.as_view(), name='delete_manifest_sub_manifest'),

    # API
    url(r'^sync_catalogs/$', csrf_exempt(views.SyncCatalogsView.as_view()), name='sync_catalogs'),

    # managedsoftwareupdate API
    url(r'^munki_repo/catalogs/(?P<name>.*)$', views.MRCatalogView.as_view()),
    url(r'^munki_repo/manifests/(?P<name>.*)$', views.MRManifestView.as_view()),
    url(r'^munki_repo/pkgs/(?P<name>.*)$', views.MRPackageView.as_view()),
    url(r'^munki_repo/icons/(?P<name>.*)$', views.MRRedirectView.as_view(section="icons")),
    url(r'^munki_repo/client_resources/(?P<name>.*)$', views.MRRedirectView.as_view(section="client_resources")),
]


main_menu_cfg = {
    'weight': 10,
    'items': (
        ('webhook', 'Webhook'),
        ('catalogs', 'Catalogs'),
        ('pkg_infos', 'PkgInfos'),
        ('manifests', 'Manifests'),
        ('sub_manifests', 'Sub manifests'),
    )
}
