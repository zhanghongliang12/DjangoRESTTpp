import uuid

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from Admin.models import AdminUser
from Admin.serializers import AdminUserSerializer
from DjangoRESTTpp.settings import ADMIN_USER_TIMOUT


class AdminUsersAPIView(CreateAPIView):
    serializer_class = AdminUserSerializer
    queryset = AdminUser.objects.filter(is_delete=False)
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        #注册
        if action =='register':
            return self.create(request,*args,**kwargs)
        #登录
        elif action =='login':
            a_username =request.data.get('a_username')
            a_password = request.data.get('a_password')
            user  =AdminUser.objects.filter(a_username =a_username)
            #判断用户是否存在
            if not user.exists():
                raise APIException(detail='用户不存在')
            #用户是否唯一
            user = user.first()
            #判断密码
            if not user.check_admin_password(a_password):
                raise APIException(detail='用户已离职')
            #uuid加密
            token = uuid.uuid4().hex#hex16 禁止
            cache.set(token,user.id,timeout =ADMIN_USER_TIMOUT)
            #返回data
            data ={
                'msg':'ok',
                'status':200,
                'token':token,
            }
            return Response(data)
        else:
            raise APIException(detail='请提供正确的动作')