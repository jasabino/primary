# Primary Challenge
Code Challenge de Automatización para Primary

## Consideraciones:

1. En las pruebas de FrontEnd - Ejercicio 1 hay dos pruebas que fallan:
    1.1 Categorías -> Belleza y Cuidado Personal -> Perfumes Importados
        No existe la subcategoria Perfumer Importados, La categoria Belleza y Cuida Personal no tiene Sub categorias
    1.2 Categorías -> Herramientas e Industria -> Industria Textil
        Hay un error en el nombre de la categoria en el enunciado deberia ser `Herramientas e Industrias`, pero se dejo la prueba fallando tal como esta en el enunciado

2. En las prueba de FrontEnd - Ejercicio 2, la prueba falla a veces, porque para algunos productos no coincide el precio, en el listado el precio esta redondeado y en el detalle del producto sale sin redondear
    Ejemplo: https://www.mercadolibre.com.ar/p/MLA15188562?pdp_filters=state:TUxBUENBUGw3M2E1%7Ccity:TUxBQ0NBUGZlZG1sYQ&source=search#position=47&type=product&tracking_id=3683ce76-bb7e-4743-8371-a839b348be47

## Pre-requisitos

Necesitaras estos programas para ejecutar el proyecto:

1. Python [(Descargar)](https://www.python.org/downloads/)
2. Pip [(Descargar)](https://pip.pypa.io/en/stable/installing/)
3. Pytest [(Install)](https://pypi.org/project/pytest/)
4. Selenium [(Install)](https://pypi.org/project/selenium/)
5. Request [(Install)](https://pypi.org/project/requests/)

## Starting

Instrucciones de Descarga Y ejecución:.

1. Clona el proyecto desde `git@github.com:jasabino/primary.git`
2. Instala los Pre-requisitos
3. Ejecuta la prueba de UI con: `pytest challengeUI.py`
4. Ejecuta la prueba de BackEnd con: `pytest challengeBE.py`


## Estructura del Proyecto

En la carpeta raiz del proyecto podras encontrar:
  - El archivo `challengeUI.py` contiene todas las pruebas de UI.
  - El archivo `challengeBE` contiene todas las pruebas de Backend.
  - la carpeta `Pages` contiene las paginas que se usan en las pruebas de UI por el patron POM.

## Construido con

* [Python](https://www.python.org/) - Lenguaje de Programación.
* [Selenium](https://www.seleniumhq.org/) -  Framework fpara automatizacion de Pruebas de Interfaz.
* [Request](https://es.python-requests.org/es/latest/) -  Framework para automatizacion de Pruebas de Backend.
* [Pytest](https://docs.pytest.org/en/latest/) - Framework de pruebas