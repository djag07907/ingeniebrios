from django import forms

from .models import Categoria, SubCategoria, Marca, \
    UnidadMedida, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripción de la Categoría",
               "estado":"Estado"}
        #widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

    def clean(self):
        
        try:
            sc = Categoria.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                
                print("Registro ya existe")
                raise forms.ValidationError("Error: Ya existe una categoria con el nombre ingresado")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Error: Ya existe una categoria con el nombre ingresado")
        except Categoria.DoesNotExist:
            pass
        return self.cleaned_data


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':"Sub Categoría",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label =  "Seleccione Categoría"
    
    def clean(self):
        try:
            sc = SubCategoria.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except SubCategoria.DoesNotExist:
            pass
        return self.cleaned_data


class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    def clean(self):
        try:
            sc = Marca.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Marca.DoesNotExist:
            pass
        return self.cleaned_data


class UMForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    def clean(self):
        try:
            sc = UnidadMedida.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except UnidadMedida.DoesNotExist:
            pass
        return self.cleaned_data


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra','descripcion','estado', \
                'precio','existencia','ultima_compra',
                'marca','subcategoria','unidad_medida']
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        try:
            sc = Producto.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk!=sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Producto.DoesNotExist:
            pass
        return self.cleaned_data

        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True