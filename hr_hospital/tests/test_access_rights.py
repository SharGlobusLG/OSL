from datetime import datetime

from odoo.exceptions import AccessError
from odoo.tests import tagged

from .common import OSLTestCommon


@tagged('post_install', '-at_install', 'osl', 'osl_access')
class TestOSLAccessRights(OSLTestCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.doctor = cls.env['osl.hospital.doctor'].create({'name': 'test_doctor'})
        cls.patient = cls.env['osl.hospital.doctor'].create({
            'name': 'test_patient',
            'doctor_id':cls.doctor
        })

        cls.appointment = cls.env['osl.hospital.appointment'].create(
            {'state': 'scheduled',
             'doctor_id': cls.doctor,
             'patient_id':cls.patient,
             'scheduled_date':datetime(2026, 1, 15, 10, 0)
             }
        )