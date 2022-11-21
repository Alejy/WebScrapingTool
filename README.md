# WebScrapingTool
Utiliza esta herramienta escrita en Python para descargar información de paginas web como listas de productos y precios, leyes y sus descripciones....
Necesitaras tener instalado python y las libreria bs4. -> pip install bs4

Modifica los parametros del script adecuandolos a tus necesidades.<br/>
Pagina Web y localización de los elementos:<br/>
* Url de la informacion que quieres reportar.<br/>
* Etiqueta que identifica cada uno de los elementos.<br/>
* Y selector de los elementos class<br/>

![image](https://user-images.githubusercontent.com/70807950/203071438-3f83f5ee-46a1-431d-84a4-78650ebf768d.png)<br/>

Indica la iformación a reportar tantos campos como desees:<br/>
* ej: nombre del producto, precio, descripción...<br/>

![image](https://user-images.githubusercontent.com/70807950/203071614-b216dd61-a7ba-4e03-a6b2-607855d155ec.png)<br/>

## Ejemplo:
###Extraeremos informacion de una lista de productos en una tienda online.
Como podemos observar cada producto esta contenido en un \<div class ="col border-0 product-item-lineal item-type-1 col-xs-12 col-sm-12 col-md-6 col-lg-4"><br/>
* Por lo tanto indicamos la url de esta pagina.<br/>
* El tipo de elemento html que lo contiene en este caso un div.<br/>
* El tipo de identificador en este caso una clase.<br/>
* El texto del identificador en este caso: col border-0 product-item-lineal item-type-1 col-xs-12 col-sm-12 col-md-6 col-lg-4<br/>
![image](https://user-images.githubusercontent.com/70807950/203073734-593a29b2-be4b-43b4-9aa7-49f4eddb3382.png)<br/>
  
 

