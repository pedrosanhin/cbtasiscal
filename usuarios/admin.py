"""Usuarios admin classes."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

# Models
from django.contrib.auth.models import User
from usuarios.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """Usuario admin."""

    list_display = ('pk', 'user')
    list_display_links = ('pk', 'user')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

    list_filter = (
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Usuario', {
            "fields": (
                ('user'),
                ('es_alumno', 'es_maestro'),
            )
        }),
    )

    readonly_fields = ('user',)

class UsuarioInLine(admin.StackedInline):
    """Usuario in-line admin for users."""

    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuarios'

class UserAdmin(BaseUserAdmin):
    """Add usuario admin to base user admin."""

    inlines = (UsuarioInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
