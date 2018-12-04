from django.test import TestCase

from stud_list.models import Student

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(name ='Big', mark= 134)

    def test_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_mark_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('mark').verbose_name
        self.assertEquals(field_label, 'mark')