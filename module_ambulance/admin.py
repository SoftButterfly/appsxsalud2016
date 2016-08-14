from django.contrib import admin
from module_ambulance.models import AmbulanceReport
from module_ambulance.models import Diagnostics


class DiagnosticsInline(admin.StackedInline):
    model = Diagnostics
    extra = 1


class AmbulanceReportAdmin(admin.ModelAdmin):
    inlines = [
        DiagnosticsInline,
    ]

    fieldsets = (
        ('Detalles de la artención', {
            'fields': (
                'date',
                'base',
                'dispatch_time',
                'departure_time_base',
                'arrival_time_focus',
                'departure_time_focus',
                'arrival_time_base',
                'emergency_priority',
                'death_place',
            )
        }),
        ('Identificación del paciente', {
            'fields': (
                'name',
                'last_name',
                'age',
                'sex',
                'identity_card',
                'insurance_type',
                'insurance_detail',
                'address',
                'address_reference',
                'district',
                'emegency_reason',
            ),
        }),
        ('Estado del paciente', {
            'fields': (
                'heart_rate',
                'breathing_frequency',
                'blood_pressure',
                'temperature',
                'o2_saturation',
                'glycemia',
                'glasgow',
                'ocular_response',
                'verbal_response',
                'motor_response',
            ),
        }),
    )

    class Meta:
        model = AmbulanceReport
        ignore = []

admin.site.register(AmbulanceReport, AmbulanceReportAdmin)
