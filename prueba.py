from  property.models import Flat
def sort_new_buildings():
    new_buildings = Flat.objects.filter(construction_year__gte=2015)
    for new_building in new_buildings:
        new_building.new_building = True
        new_building.save()
    old_buildings = Flat.objects.filter(construction_year__lt=2015)
    for old_building in old_buildings:
        old_building.new_building = False
        old_building.save()
