from .models import MyUser

from django.db.models import Q

from rest_framework.serializers import(
    ValidationError,
    EmailField,
    CharField,
    ModelSerializer
)


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'city',
            'position',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        position=validated_data['position']
        city=validated_data['city']
        password = validated_data['password']
        user_obj = MyUser(
            username=username,
            email=email,
            position=position,
            city=city,
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'position',
            'city',
        ]



class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label = 'Email adress',required=False, allow_blank=True)
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login.")

        user = MyUser.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        data["token"] = "SOME RANDOM TOKEN"
        return data


class UserListSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'position',
            'city',
        ]

