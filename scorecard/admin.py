from django.contrib import admin
from .models import Match, Score, Team
# Register your models here.


admin.site.register(Team)
admin.site.register(Match)

class ScoreAdmin(admin.ModelAdmin):
    change_list_template = 'admin/scorecard/change_form.html'

admin.site.register(Score)
