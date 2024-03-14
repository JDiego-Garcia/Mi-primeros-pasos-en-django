from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTest(TestCase):
    
    def setUp(self):
        
        instance = Post.objects.create(title='Curso de django', description ='....')
        instance.save()
        
    
        instance = Post.objects.create(title='Angular vs react')
        instance.save()
        
        instance = Post.objects.create(title='Prueba', subtitle ='pruebita')
        instance.save()
        
        
    def test_for_post(self):
        print(Post.objects.all()) #imprime todos los objetos
        print(Post.objects.filter(title='Curso de django')) # filtra imprime solo si el titulo corresponde a lo que ponemos 
        
        print('################')
        print('SOLO LO QUE CONTIENE CURSO')
        print(Post.objects.filter(title__icontains='Curso')) # filtra e imprime solo si contiene la palabra curso
                                                            # el i es para que no sea case_sensitive
        #print(Post.objects.filter(created_at_range=['2024-02-01', '2024-03-20'])) #filtra e imprime por fecha de creacion
        
        print(Post.objects.get(pk=2)) #imprime el titulo con respecto a la llave primaria 
        instance = Post.objects.get(pk=2) #asignamos el valor del id2 a la variable instance
        instance.title = 'Django rest' # le cambiamos el valor
        instance.save() #importante guardar despues de cada cambio
        
        print('################')
        print(Post.objects.get(pk=2)) #mostramos cambios
        
        print('MOSTRANDO TODO DE NUEVO')
        print(Post.objects.all())
        
        print('Borrando #####')
        instance.delete()
        print(Post.objects.all())
        
        