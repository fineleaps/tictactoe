from django.contrib import admin
from .models import Campaign, Prospect, Lead, DNC, Executive


# class ExecutiveInline(admin.TabularInline):
#     model = Executive


class CampaignAdmin(admin.ModelAdmin):

    list_display = ('name', 'active_status', 'start_date', 'end_date')
    # inlines = [ExecutiveInline, ]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Prospect)
admin.site.register(Lead)
admin.site.register(DNC)
admin.site.register(Executive)
