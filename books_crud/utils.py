import re 
from .models import Author

def get_the_index_of_author(request):
    request_author = request.data['author']
    is_author = Author.objects.filter(author= request_author)
    
    if is_author:
        auther_index = str(is_author.first())
        auther_index_int = re.findall('[0-9]+',auther_index)
        return int(auther_index_int[0])
    else:
        author_obj = Author.objects.create(author=request_author)
        auther_index_new = str(author_obj)
        auther_index_int_new = re.findall('[0-9]+',auther_index_new)
        return int(auther_index_int_new[0])