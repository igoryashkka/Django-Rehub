from rest_framework import serializers
from .models import Microcontoller
from datetime import datetime

class HardwareSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Microcontoller
        fields = ('title', 'mcu_qty')
        # or you can use , for all atributes:  
        #fields = '__all__'
