from django.db import models
from django.core.exceptions import ValidationError

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo
from inv.models import Producto
# VALIDACIONES START
def validarnombre(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"or lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"or lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="."or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡"):
             raise ValidationError('Nombre incorrecto, solo se permite ingresar letras')
        n=n+1
    
    
    
    if (len(lista))<2:
        raise ValidationError('El texto es inválido debe ser mayor a 3 caracteres, digite de nuevo')
    
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
        raise ValidationError('El texto debe ser válido digite de nuevo')

def validarnumero(value):
    numeros=[]
    n=0
    for indice in value:
        numeros.append(indice)
        if(numeros[n]!="0" and numeros[n]!="1" and numeros[n]!="2" and numeros[n]!="3" and numeros[n]!="4" and numeros[n]!="5" and numeros[n]!="6" and numeros[n]!="7" and numeros[n]!="8" and numeros[n]!="9")>0:
            raise ValidationError('El número no puede contener letras')
        n=n+1

def validarnumerotelefono(value):
    numeros=[]
    n=0
    for indice in value:
        numeros.append(indice)
        if(numeros[n]!="0" and numeros[n]!="1" and numeros[n]!="2" and numeros[n]!="3" and numeros[n]!="4" and numeros[n]!="5" and numeros[n]!="6" and numeros[n]!="7" and numeros[n]!="8" and numeros[n]!="9"):
            raise ValidationError('El número no puede contener letras')
        n=n+1
        
    if ((numeros[0]=="0") or (numeros[0]=="1") or (numeros[0]=="4") or (numeros[0]=="5") or (numeros[0]=="6")):
        raise ValidationError('El número no es válido, intente de nuevo')
    if(len(numeros))<8:
        raise ValidationError('El número debe contener al menos 8 dígitos, intente de nuevo')
    if("-" in numeros or ("." in numeros)):
        raise ValidationError('El número debe contener al menos 8 dígitos, ejemplo 99234567')

# def validardireccion(value):
#     lista=[]
#     n=0
#     for indice in value:
#         lista.append(indice)
#         if(lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]=="" or lista[n]=="#" or lista[n]=="$" or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·" ):
#             raise ValidationError('Nombre incorrecto, solo se permite ingresar letras')
#         n=n+1
    
#     # if(len(lista)<100):
#     #     raise ValidationError('La dirección debe contener al menos 30 caracteres')
#     # if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
#     #     raise ValidationError('La dirección debe ser válida digite de nuevo debe contener al menos 1 vocal')

#     # if lista[0]=="." or lista[0]==",":
#     #    raise ValidationError('La dirección no puede contener un punto al inicio')
    
#     # lista=[]
#     # vocal=["a","e","i","o","u","á","é","í","ó","ú"]
#     # cont=0
#     # for i in vocal:
#     #     for j in value:
#     #         if(i==j):
#     #             cont+=1
#     # if(cont<1):
#     #  raise ValidationError('El texto es inválido, debe contener vocales digite de nuevo')

def validarcorreoexistenteProveedor(value):
    listaE = Proveedor.objects.all()
    for data in listaE:
        if(data.Correo_Proveedor==value):
            raise ValidationError('El correo ya existe')  



# VALIDACIONES END

class Proveedor(ClaseModelo):
    descripcion=models.CharField(
        max_length=50,
        unique=True,validators=[validarnombre]
        )
    direccion=models.CharField(
        max_length=100,
        null=True, blank=True,
    
    )
    contacto=models.CharField(
        max_length=100,
        null=True,blank=True,
        validators=[validarnombre]
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True,
        validators=[validarnumerotelefono]
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True,
       
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"


class ComprasEnc(ClaseModelo):
    fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.CharField(max_length=100,validators=[validarnumero])
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"



@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender,instance, **kwargs):
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()
    if enc:
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total=sub_total['sub_total__sum']
        enc.descuento=descuento['descuento__sum']
        enc.save()
    
    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.id
    fecha_compra=instance.compra.fecha_compra

    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.ultima_compra=fecha_compra
        prod.save()


