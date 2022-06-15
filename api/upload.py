import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

fs = FileSystemStorage(location='tmp/')


@api_view(['POST'])
def upload_data(request):
    file = request.FILES['file']

    content = file.read()

    file_content = ContentFile(content)
    file_name = fs.save('_tmp.csv', file_content)
    tmp_file = fs.path(file_name)

    csv_file = open(tmp_file, errors='ignore')
    reader = csv.reader(csv_file)
    next(reader)

    line = next(reader)
    province = line[0][11:]
    municipality = line[4][11:]
    district = line[16][10:]

    line = next(reader)
    name = line[0][8:]
    code = line[1][8:]

    line = next(reader)
    sector = line[0][47:]

    line = next(reader)
    subordinate = line[0][49:]
    core = Core(code=code, name=name, municipality=municipality, province=province,
                district=district, sector=sector, subordinate=subordinate)

    try:
        core.save()
    except core.DoesNotExist:
        pass

    for i in range(4):
        next(reader)

    militant_list = []
    for id_, row in enumerate(reader):
        ci = row[0]
        name = row[1]
        first_lastname = row[2]
        second_lastname = row[3]

        street = row[41]
        apto = row[42]
        corner = row[43]
        neighborhood = row[44]
        municipality = row[45]
        province = row[46]
        address = Address(street=street, apto=apto, corner_or_ave=corner, neighborhood=neighborhood,
                          municipality=municipality, province=province)

        try:
            address.save()
            militant = Militant(
                ci, name, first_lastname, second_lastname, address=address, core=core)
        except address.DoesNotExist:
            pass
        except ValueError:
            militant = Militant(
                ci, name, first_lastname, second_lastname, core=core)

        try:
            militant.save()
        except militant.DoesNotExist:
            pass
        except ValueError:
            pass

    csv_file.close()
    fs.delete(file_name)
    return Response({'detail': 'Succesfully uploaded the data'})
