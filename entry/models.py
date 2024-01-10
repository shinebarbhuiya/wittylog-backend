from django.db import models
# from django.contrib.auth.models import User

# from authentication.models import CustomUser

from pgvector.django import VectorField

from .customs.nanoid import generate_nanoid
from .customs.current_date import current_datatime

from .customs.vectors import create_vector_from_content, split_texts

from django.db import transaction
from rest_framework.authtoken.models import Token
from django.conf import settings








class Entry(models.Model):
    id = models.CharField(primary_key=True, default=generate_nanoid , max_length=21,  editable=False)
    title = models.CharField(max_length=200, editable=False, default=current_datatime )
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title


    def save(self,  *args, **kwargs):

        if not self.pk:  # This is a new entry
            request = kwargs.pop('request', None)
            if request:
                token = request.META.get('HTTP_AUTHORIZATION', '').split()[1]
                user = Token.objects.get(key=token).user

                print(user)
                self.author = user


        #  block ensures that the deletion and saving operations are atomic, meaning they either all succeed or fail together.
        with transaction.atomic():
            # Delete existing EntryEmbedding instances
            self.entryembedding_set.all().delete()

            # Save the Entry instance
            super(Entry, self).save(*args, **kwargs)

            # Create new EntryEmbedding instances
            chunks = split_texts(f"""Date : {self.title}\n Entry: {self.content}""")
            for chunk in chunks:
                embedding = create_vector_from_content(chunk)
                EntryEmbedding.objects.create(entry=self, embedding=embedding, text=chunk)
    

    
    

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.title = timezone.now().strftime('%A, %b %d, %Y')

    #     super(Entry, self).save(*args, **kwargs) 

class EntryEmbedding(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, blank=True, null=True)
    embedding = VectorField(dimensions=1024)  # This field type is a guess.
    text = models.CharField(blank=True, null=True)
    id = models.CharField(primary_key=True, default=generate_nanoid , max_length=21,  editable=False)

    # def save(self, *args, **kwargs):
    #     self.vector_data = create_vector_from_content(self.content)
    #     super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.entry)
    
    # class Meta:
    #     managed = False
    #     db_table = 'entry_entryembedding'

  

    
