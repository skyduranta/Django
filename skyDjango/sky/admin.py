from django.contrib import admin
from .models import SkyColor, SkyReview, Season, PhotoCertificate


# Register your models here.
class SkyReviewInline(admin.TabularInline):
    model = SkyReview
    extra = 1


class SkyColorAdmin(admin.ModelAdmin):
    list_display = ("color", "type", "date_added")
    inlines = [SkyReviewInline]


class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("sky_varieties",)


class PhotoCertificateAdmin(admin.ModelAdmin):
    list_display = ("sky", "certificate_number", "issued_date", "valid_until")


admin.site.register(SkyColor, SkyColorAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(PhotoCertificate, PhotoCertificateAdmin)

# admin.site.register(SkyColor)
