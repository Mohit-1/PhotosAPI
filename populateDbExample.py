import requests
from photos.models import Photo, Group

group_list = ['1577604@N20', '16978849@N00', '34427469792@N01']

# WARNING! Enter your API key in the query parameter for the below two URLs
url_by_group = """https://api.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&api_key=<your_api_key_here>&group_id={0}&format=json&nojsoncallback=1"""
url_by_photo = """https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=<your_api_key_here>&photo_id={0}&format=json&nojsoncallback=1"""

for group_id in group_list:
    group = Group(name=group_id)
    group.save()

    count = 0
    response_by_group = requests.get(url_by_group.format(group_id), timeout=5)
    print(response_by_group.content)
    pic_list = response_by_group.json()['photos']['photo']

    for pic in pic_list:
        response_by_photo = requests.get(url_by_photo.format(pic['id']), timeout=5)
        owner = response_by_photo.json()['photo']['owner']['username']
        title = response_by_photo.json()['photo']['title']['_content']
        url = response_by_photo.json()['photo']['urls']['url'][0]['_content']

        photo = Photo(pid=int(pic['id']), title=title, photo_url=url, owner=owner, group=group)
        photo.save()
        count += 1

    group.no_of_photos = count
    group.save()