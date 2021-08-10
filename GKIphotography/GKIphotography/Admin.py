
from django.contrib import admin
from app import models 

class GKiphotographyAdmin(admin.AdminSite):
    site_header = 'GKI photography Admin'


adminSite = GKiphotographyAdmin(name ='GKIadmin')

admin.site.site_header = 'GKIphotography Admin'
admin.site.register(models.Category)
admin.site.register(models.Photo)
admin.site.register(models.Video)
admin.site.register(models.homePageBackground)
admin.site.register(models.DroneDescription)
admin.site.register(models.photoCollection)
admin.site.register(models.AboutUs)
admin.site.register(models.ContactUs)