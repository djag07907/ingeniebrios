from django.db import models

from django.core.exceptions import ValidationError
from bases.models import ClaseModelo
from django.utils.encoding import smart_str


# VALIDACIONES START
def validarnombre(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"or lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"or lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="."or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"):
             raise ValidationError("Nombre incorrecto, solo se permite ingresar letras")
        n=n+1
    
    
    
    if (len(lista))<2:
        raise ValidationError('El texto es inv&aacute;lido debe ser mayor a 3 caracteres, digite de nuevo')
    
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c" :
        raise ValidationError('El texto debe ser válido digite de nuevo')

def validarnumero(value):
    numeros=[]
    n=0
    for indice in value:
        numeros.append(indice)
        if(numeros[n]!="0" and numeros[n]!="1" and numeros[n]!="2" and numeros[n]!="3" and numeros[n]!="4" and numeros[n]!="5" and numeros[n]!="6" and numeros[n]!="7" and numeros[n]!="8" and numeros[n]!="9")>0:
            raise ValidationError('El número no puede contener letras')
        n=n+1



# VALIDACIONES END
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        help_text='Descripción de la Categoría',
        unique=True,
        
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
  

    class Meta:
        verbose_name_plural= "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=50,
        help_text='Descripción de la Categoría',
        
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    
    

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):


    def autonumber_productCode():
        last_product = Producto.objects.all().order_by('id').last()
        if not last_product:
            return 'PR-00000'
        product_id = last_product.codigo
        product_int = int(product_id[4:8])
        new_product_int = product_int + 1
        new_product_id = 'PR-' + str(new_product_int).zfill(5)
        return new_product_id

    def autonumber_SKUCode():
        last_SKU = Producto.objects.all().order_by('id').last()
        if not last_SKU:
            return 'SKU-0000000000'
        SKU_id = last_SKU.codigo
        SKU_int = int(SKU_id[5:14])
        new_SKU_int = SKU_int + 1
        new_SKU_id = 'SKU-' + str(new_SKU_int).zfill(10)
        return new_SKU_id    

    codigo = models.CharField(
        max_length=20,
        unique=True,
        #validators=[validarnumero]
        default= autonumber_productCode
    )
    codigo_barra = models.CharField(max_length=50, default= autonumber_SKUCode)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')