from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff, Loan, Status

# Register your models here.

# create a table of Loan instances
class LoanInLine(admin.TabularInline):
    model = Loan
    fk = 'user_id'
    readonly_fields = ('loan_amount', 'date', 'status')
    fields = ('loan_amount', 'date', 'status')
    extra = 0
    can_delete = False


# Set up the staff interface for the admin site
class StaffAdmin(UserAdmin):
    inlines = [LoanInLine]
    list_display = ['username', 'first_name', 'last_name', 'phone', 'account_name', 'account_number']

    def has_module_permission(self, request):
        return request.user.is_superuser
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'account_name', 'account_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser'), 'classes': ('collapse',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined'), 'classes': ('collapse',)}),
    )


# create a customized loan filter
class PendingLoanFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'pending':
            return queryset.filter(status=3) # 3 represents "pending"
        elif self.value() == 'approved':
            return queryset.filter(status=2) # 2 represents "pending"
        elif self.value() == 'rejected':
            return queryset.filter(status=1) # 1 represents "pending"
        
        return queryset


class LoanAdmin(admin.ModelAdmin):
    list_filter = (PendingLoanFilter,)


admin.site.register(Staff, StaffAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Status)
