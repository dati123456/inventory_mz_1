from rest_framework import serializers
from .models import Item, Category
from datetime import date


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = '__all__'


    @staticmethod
    def special_caracters(value, field_name):
        special_characters = '!@#$%^&*'
        for char in special_characters:
            if char in value:
                raise serializers.ValidationError(f"{field_name} cannot contain special characters [!@#$%^&*].")



    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("saxeli unda iyos 5 asoze meti")
        self.special_caracters(value, 'Name')

        return value

    def validate_description(self, value):
        if len(value.split()) < 2:
            raise serializers.ValidationError("unda iyos 2ze meti sityva")
        self.special_caracters(value, 'Description')
        return value

    def validate_expiration_requaiment(self,data):

        if data['category'] and any(word in data['category'].name.lower() for word in ['food', 'drink']) and not data[
            'expiration_date']:
            raise serializers.ValidationError("vada aucilebelia am kategoriistvis.")

        return data


    def validate_expiration_date(self, value):
        request = self.context.get('request')
        if value and value < date.today():
            raise serializers.ValidationError("ar sheidzleba iyos warsuli dro")

        return value

    def validate_dimentions(self, data):
        numeric_fields = ['width', 'height', 'length', 'weight']
        for field in numeric_fields:
            if data.get(field) and data.get(field) <= 0:
                raise serializers.ValidationError({field: f"{field.capitalize()} ar sheileba iyos nuli an negatiuri ricxvi."})

        return data
