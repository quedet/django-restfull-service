from rest_framework import serializers
from drones.models import Competition, Drone, DroneCategory, Pilot

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='drone-detail'
    )

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'slug',
            'drones'
        )

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # Display the category name
    drone_category = serializers.SlugRelatedField(slug_field='name', queryset=DroneCategory.objects.all())

    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'slug',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            'created'
        )

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone'
        )

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'created',
            'competitions'
        )

class PilotCompetitionSerializer(serializers.ModelSerializer):
    # Display the pilot's name
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone'
        )