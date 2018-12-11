from rest_framework import serializers

from Admin.models import AdminUser


class  AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        Model=AdminUser
        fields =('a_user_name','a_password')
    def post(self,request):
        pass
