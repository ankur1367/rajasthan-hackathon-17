from .models import Info, FamilyInfo
from rest_framework import serializers

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        # fields = ('category', 'aadhar', 'state', 'hof_name', 'house_number',
        # 'relations', 'date_of_birth', 'eco_group', 'building_number', 'bhamasha_id',
        # 'street_name', 'ifsc_code', 'my_id', 'family_idno', 'pincode', 'landline_no',
        # 'village_name', 'gp_ward', 'email', 'spouse_name', 'is_rural',
        # 'district', 'edu_info', 'account_number', 'address', 'income', 'bank_name',
        # 'landmark', 'ration_card_no', 'name_extra', 'mobile_no', 'gender', 'father_name',
        # 'fax_no', 'block_city', 'created_date',)

class FamilyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInfo
        # fields = ('family', 'category', 'aadhar', 'state', 'hof_name', 'house_number',
        # 'relations', 'date_of_birth', 'eco_group', 'building_number', 'bhamasha_id',
        # 'street_name', 'ifsc_code', 'my_id', 'family_idno', 'pincode', 'landline_no',
        # 'village_name', 'gp_ward', 'email', 'spouse_name', 'is_rural',
        # 'district', 'edu_info', 'account_number', 'address', 'income', 'bank_name',
        # 'landmark', 'ration_card_no', 'name_extra', 'mobile_no', 'gender', 'father_name',
        # 'fax_no', 'block_city', 'created_date',)
        fields = '__all__'
