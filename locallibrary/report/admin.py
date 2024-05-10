from django.contrib import admin

# Register your models here.
from .models import DocuementReport , ReferenceReport
 
class DocumentReportAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'name', 'docid')
    fields = ['clientid', 'name', 'docid']
    #not allowing to edit fields after first use
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('name', 'docid')
        return self.readonly_fields
    #readonly_fields = ('name', 'docid',)

    
admin.site.register(DocuementReport , DocumentReportAdmin)

class ReferenceReportAdmin(admin.ModelAdmin):
    list_display = ('clientid', 'name', 'caseid')
    fields = ['clientid', 'name', 'caseid']
    
    
admin.site.register(ReferenceReport , ReferenceReportAdmin)