from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MaxLengthValidator
import uuid
from django.utils import timezone


class AmbulanceReport(models.Model):

    # Datos del reporte
    id = models.UUIDField(
        _("Código de idnetificacion"),
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )

    creation_date = models.DateTimeField(
        _("Fecha de Creación"),
        default=timezone.now,
        editable=False,
    )

    last_modified = models.DateTimeField(
        _("Última Modificación"),
        default=timezone.now,
        editable=False,
    )

    # Datos de la movilizacion de la ambiulancia:
    date = models.DateField(
        _("Fecha"),
        blank=True,
        null=True,
    )

    base = models.CharField(
        _("Base de unidad"),
        max_length=256,
        blank=True,
        null=True,
    )

    dispatch_time = models.TimeField(
        _("Hora de despacho"),
        blank=True,
        null=True,
    )

    departure_time_base = models.TimeField(
        _("Hora de salida desde la base"),
        blank=True,
        null=True,
    )

    arrival_time_focus = models.TimeField(
        _("Hora de llegada al foco"),
        blank=True,
        null=True,
    )

    departure_time_focus = models.TimeField(
        _("Hora de salida desde el foco"),
        blank=True,
        null=True,
    )

    arrival_time_base = models.TimeField(
        _("Hora de llegada a la base"),
        blank=True,
        null=True,
    )

    # Detalles de la emergencia
    EMERGENCY_PRIORITY_CHOICES = (
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
    )

    emergency_priority = models.IntegerField(
        _("Prioridad de la emergencia"),
        blank=True,
        null=True,
        choices=EMERGENCY_PRIORITY_CHOICES,
    )

    DEATH_PLACE_CHICES = (
        (0, ""),
        (1, "En el foco"),
        (2, "Durante el traslado"),
    )

    death_place = models.IntegerField(
        _("Fallecido"),
        blank=True,
        null=True,
        default=0,
        choices=DEATH_PLACE_CHICES,
    )

    # Datos de paciente
    name = models.CharField(
        _("Nombres"),
        max_length=64,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        _("Apellidos"),
        max_length=64,
        blank=True,
        null=True
    )

    age = models.IntegerField(
        _("edad"),
        blank=True,
        null=True,
    )

    SEX_CHOICES = (
        (0, "Masculino"),
        (1, "Femenino"),
    )

    sex = models.IntegerField(
        _("Sexo"),
        blank=True,
        null=True,
        choices=SEX_CHOICES,
    )

    identity_card = models.IntegerField(
        _("Documento de identidad"),
        blank=True,
        null=True,
    )

    INSURANCE_TYPE_CHOICES = (
        (1, "SIS"),
        (2, "ESSALUD"),
        (3, "SOAT"),
        (4, "EPS"),
        (5, "SIN SEGURO"),
        (6, "OTRO"),
    )

    insurance_type = models.IntegerField(
        _("Tipo de seguro"),
        blank=True,
        null=True,
        choices=INSURANCE_TYPE_CHOICES,
    )

    insurance_detail = models.CharField(
        _("Detalle del seguro"),
        help_text=_("Aplicable solo si el tipo de seguro es 'OTROS'"),
        max_length=64,
        blank=True,
        null=True
    )

    address = models.CharField(
        _("Dirección"),
        max_length=128,
        blank=True,
        null=True
    )

    address_reference = models.CharField(
        _("Referencia"),
        max_length=128,
        blank=True,
        null=True,
    )

    district = models.CharField(
        _("Distrito"),
        max_length=128,
        blank=True,
        null=True
    )

    emegency_reason = models.TextField(
        _("Motivo de la emergencia"),
        max_length=1024,
        validators=[
            MaxLengthValidator(1024),
        ],
        blank=True,
        null=True
    )

    # Condicion del Paciente
    heart_rate = models.CharField(
        _("Frecuencia cardiaca"),
        max_length=255,
        blank=True,
        null=True,
    )

    breathing_frequency = models.CharField(
        _("Frecuencia respiratoria"),
        max_length=255,
        blank=True,
        null=True,
    )

    blood_pressure = models.CharField(
        _("Presion arterial"),
        max_length=255,
        blank=True,
        null=True,
    )

    temperature = models.CharField(
        _("Temperatura"),
        max_length=255,
        blank=True,
        null=True,
    )

    o2_saturation = models.CharField(
        _("Saturación de O2"),
        max_length=255,
        blank=True,
        null=True,
    )

    glycemia = models.CharField(
        _("Glicemia"),
        max_length=255,
        blank=True,
        null=True,
    )

    glasgow = models.CharField(
        _("Glasgow"),
        max_length=255,
        blank=True,
        null=True,
    )

    ocular_response = models.CharField(
        _("Respuesta ocular"),
        max_length=255,
        blank=True,
        null=True,
    )

    verbal_response = models.CharField(
        _("Respuesta verbal"),
        max_length=255,
        blank=True,
        null=True,
    )

    motor_response = models.CharField(
        _("Respuesta motora"),
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Ficha de atención prehospitalaria"  # _("Ambulance Report")
        verbose_name_plural = "Fichas de atención prehospitalaria"  # _("Ambulance Reports")

    def __str__(self):
        if self.id is None:
            return "{0} sin registrar".format(self._meta.verbose_name.capitalize())

        return "{0} {1} (registrada el {2} a las {3})".format(
            self._meta.verbose_name.capitalize(),
            self.id.hex,
            self.creation_date.strftime('%Y-%m-%d'),
            self.creation_date.strftime('%H:%M:%S')
        )


class Diagnostics(models.Model):
    id = models.UUIDField(
        _("Código de idnetificacion"),
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )

    diagnostics = models.TextField(
        _("Diagnostico"),
        validators=[
            MaxLengthValidator(1024),
        ],
        blank=True,
        null=True
    )

    ambulance_report = models.ForeignKey(
        AmbulanceReport,
        verbose_name=_("Ficha de atencion prehospitalaria"),
        on_delete=models.PROTECT,
        related_name="diagnostic",
        related_query_name="ambulance_reports",
    )

    class Meta:
        verbose_name = "Diagnostico"  # _("Ambulance Report")
        verbose_name_plural = "Diagnosticos"  # _("Ambulance Reports")

    def __str__(self):
        if self.id is None:
            return "{0} sin registrar".format(self._meta.verbose_name.capitalize())

        return "Diagnostico de {0} {1} (registrada el {2} a las {3})".format(
            self.ambulance_report._meta.verbose_name.lower(),
            self.ambulance_report.id.hex,
            self.ambulance_report.creation_date.strftime('%Y-%m-%d'),
            self.ambulance_report.creation_date.strftime('%H:%M:%S')
        )
