from django.test import TestCase
from django.urls import reverse

from stud_list.models import Student

class TableTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_students = 13

        for student_id in range(number_of_students):
            Student.objects.create(
                name =f'Christian {student_id}',
                mark =53,
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)


    
           
    