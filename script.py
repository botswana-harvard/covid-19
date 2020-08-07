import csv
from covid19_register.models.employee import Employee

from django.db import IntegrityError

with open('Contact.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        first_name, last_name, cell = line

        try:
            Employee.objects.create(first_name=first_name, last_name=last_name,
                                    cell=cell)
        except IntegrityError:
            pass
