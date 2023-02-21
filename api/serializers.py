from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    origin = serializers.TextField("Origin")
    origins = serializers.TextField("Origins")
    destination = serializers.TextField("destination")
    destinations = serializers.TextField("destinations")
    
    q = serializers.TextField("q")
    gl = serializers.TextField("gl")
    hl = serializers.TextField("hl")
    autocorrect = serializers.Boolean("autocorrect")    
    
    class Meta:
        fields = ['__all__']

    # def validate(self, attrs):
    #     new = attrs.get('new_password')
    #     new2 = attrs.get('confirm_new')
    #     if new != new2:
    #         raise serializers.ValidationError("Password didn't match")
    #     return super().validate(attrs)