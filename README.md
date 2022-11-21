# WebScrapingTool
Utiliza esta herramienta escrita en Python para descargar información de p'aginas web como listas de productos y precios, leyes y sus descripciones....<br/>
Necesitaras tener instalado python y las librería bs4. -> pip install bs4<br/>

Modifica los parámetros del script adecuándolos a tus necesidades.<br/>
Página Web y localización de los elementos:<br/>
* Url de la información que quieres reportar.<br/>
* Etiqueta que identifica cada uno de los elementos.<br/>
* Y selector de los elementos class<br/>

![image](https://user-images.githubusercontent.com/70807950/203071438-3f83f5ee-46a1-431d-84a4-78650ebf768d.png)<br/>

Indica la información a reportar tantos campos como desees:<br/>
* ej: nombre del producto, precio, descripción...<br/>

![image](https://user-images.githubusercontent.com/70807950/203071614-b216dd61-a7ba-4e03-a6b2-607855d155ec.png)<br/>

## Ejemplo:
##Extraeremos información de una lista de productos en una tienda online.<br/>
Como podemos observar cada producto esta contenido en un \<div class ="col border-0 product-item-lineal item-type-1 col-xs-12 col-sm-12 col-md-6 col-lg-4"><br/>
* Por lo tanto indicamos la url de esta página.<br/>
* El tipo de elemento html que lo contiene en este caso un div.<br/>
* El tipo de identificador en este caso una clase.<br/>
* El texto del identificador en este caso: col border-0 product-item-lineal item-type-1 col-xs-12 col-sm-12 col-md-6 col-lg-4<br/>
![image](https://user-images.githubusercontent.com/70807950/203073734-593a29b2-be4b-43b4-9aa7-49f4eddb3382.png)<br/>

Para indicar los campos que queremos recuperar utilizamos la herramienta de desarrollador:<br/>
* En nuestro caso queremos recuperar el precio del producto.<br/>
* Primero indicamos el nombre del dato: en nuestro caso price<br/>
* Segundo Indicamos el tipo de etiquera html que lo contiene: span<br/>
* Tercero indicamos el tipo de selector id o class: en nuestro caso class<br/>
* Cuarto indicamos el texto del selector: price-offer-now<br/>

![image](https://user-images.githubusercontent.com/70807950/203076317-70c05b63-b26e-4cc2-b4f1-5db05d523a69.png)<br/>

![image](https://user-images.githubusercontent.com/70807950/203076002-ca4faf7d-3243-499e-b983-800ddb919313.png)<br/>

 

