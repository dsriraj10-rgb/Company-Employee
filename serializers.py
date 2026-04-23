from api.models import Company, Employee
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        company_id=serializers.ReadOnlyField()
        model = Company
        fields = '__all__'
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        employee_id=serializers.ReadOnlyField()
        model = Employee
        fields = '__all__'