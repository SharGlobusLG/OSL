from odoo.tests import TransactionCase, new_test_user


class OSLTestCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Book = cls.env['odoo.school.library.book']

        group_patient = 'odoo_school_library.odoo_school_library_group_user'
        group_manager = 'odoo_school_library.odoo_school_library_group_manager'
        cls.patient = new_test_user(cls.env, login='osl_patient', groups=group_patient)

        cls.manager = new_test_user(cls.env, login='osl_manager', groups=group_manager)

        cls.employee = new_test_user(cls.env, login='test_employee', groups='base.group_user')

        # cls.author = cls.env['res.partner'].create({'name': 'Test Author'})
        # cls.reader = cls.env['res.partner'].create({'name': 'Test Reader'})