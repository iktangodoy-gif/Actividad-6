# ACTIVIDAD 6

## Desarrollo de Bases de Datos DML y DDL

**Programa:** Técnico en Programación de Software
**Proyecto formativo:** Construcción de sistema de información para emprendedores y empresarios.
**Competencia:** Administrar la base de datos de acuerdo a los estándares y requisitos técnicos del cliente.

---

# 1. ENTREVISTA A 5 COMPAÑEROS

Para esta actividad se realizó una entrevista a cinco compañeros de clase con el objetivo de recopilar información básica como nombres, apellidos, sexo y edad.

## Datos básicos

| Nombres | Apellidos | Sexo      | Edad |
| ------- | --------- | --------- | ---- |
| Carlos  | Rodríguez | Masculino | 17   |
| María   | González  | Femenino  | 16   |
| Juan    | Martínez  | Masculino | 17   |
| Laura   | Pérez     | Femenino  | 16   |
| Andrés  | Gómez     | Masculino | 18   |

> **Nota:** Los datos anteriores son ejemplos y deben ser reemplazados por los datos reales de los compañeros entrevistados.

## Preguntas sobre gustos y características

También se realizaron preguntas relacionadas con:

* Canción o género musical favorito.
* Película favorita.
* Deporte favorito.
* Materia favorita.
* Comida favorita.
* Fortalezas.
* Debilidades.

| Compañero | Música   | Película     | Deporte    | Materia      | Comida      | Fortaleza         | Debilidad   |
| --------- | -------- | ------------ | ---------- | ------------ | ----------- | ----------------- | ----------- |
| Carlos    | Reguetón | Spider-Man   | Fútbol     | Matemáticas  | Pizza       | Responsabilidad   | Timidez     |
| María     | Pop      | Barbie       | Voleibol   | Inglés       | Pasta       | Creatividad       | Nervios     |
| Juan      | Rap      | Avengers     | Fútbol     | Programación | Hamburguesa | Liderazgo         | Impaciencia |
| Laura     | Pop      | Enola Holmes | Natación   | Biología     | Sushi       | Organización      | Distracción |
| Andrés    | Rock     | Interestelar | Baloncesto | Física       | Pollo       | Trabajo en equipo | Desorden    |

---

# 2. CHATBOT DE VOZ EN STREAMLIT

## Objetivo

Desarrollar un chatbot de voz utilizando la información recopilada durante las entrevistas. La personalidad del chatbot estará basada en la combinación de los gustos, fortalezas y características de los cinco compañeros.

## Personalidad del chatbot

El chatbot se llamará **Compabot**.

Compabot tendrá una personalidad amigable, creativa, responsable y colaborativa. Podrá conversar sobre música, películas, deportes, comida, programación y diferentes materias académicas.

La personalidad será una combinación de las características encontradas en las entrevistas.

## Ejemplo

**Usuario:** ¿Qué deportes te gustan?

**Compabot:** Me gustan diferentes deportes como el fútbol, voleibol, natación y baloncesto, porque mi personalidad combina las preferencias de diferentes compañeros.

**Usuario:** ¿Qué materias te gustan?

**Compabot:** Me interesan materias como programación, matemáticas, inglés, biología y física.

## Comparación con otros chatbots

Existen diferentes chatbots que utilizan personalidades configuradas para interactuar con los usuarios de una manera determinada.

Nuestro chatbot tiene una característica particular: su personalidad se construye a partir de la combinación de la información obtenida de cinco estudiantes entrevistados.

El chatbot será desarrollado y desplegado utilizando **Streamlit**.

---

# 3. PROYECTO IoT: COINK

COINK es un proyecto relacionado con Internet de las Cosas (IoT), en el cual se utilizan máquinas llamadas **Oinks** para que las personas puedan realizar depósitos de dinero y llevar estos ahorros a una billetera digital.

## 3.1 Métrica para evaluar usuarios

Para analizar los datos de los depósitos se propone crear un **Índice de Ahorro del Usuario (IAU)**.

Este índice puede tener en cuenta:

* Cantidad de depósitos.
* Valor total ahorrado.
* Promedio de cada depósito.
* Frecuencia de los depósitos.

Una propuesta de fórmula es:

**IAU = (Valor total ahorrado × 0,5) + (Número de depósitos × 0,3) + (Promedio por depósito × 0,2)**

La métrica permitirá clasificar a los usuarios según su comportamiento de ahorro.

### Clasificación

| Puntaje  | Clasificación |
| -------- | ------------- |
| 0 - 30   | Bajo          |
| 31 - 60  | Medio         |
| 61 - 80  | Alto          |
| 81 - 100 | Muy alto      |

Para el análisis de los datos se utilizarán herramientas como:

* Python.
* Pandas.
* Matplotlib.
* Streamlit.

También se desarrollarán gráficas para representar los resultados obtenidos.

---

# 3.2 BASE DE DATOS RELACIONAL Y NO RELACIONAL

## Base de datos relacional

Una base de datos relacional organiza la información mediante tablas que pueden estar relacionadas entre sí.

Por ejemplo, se pueden tener las tablas:

### Usuarios

| ID | Nombre | Edad |
| -- | ------ | ---- |
| 1  | Carlos | 17   |
| 2  | María  | 16   |

### Depósitos

| ID | ID Usuario | Valor   |
| -- | ---------- | ------- |
| 1  | 1          | $5.000  |
| 2  | 1          | $10.000 |
| 3  | 2          | $20.000 |

La relación entre ambas tablas se realiza mediante el ID del usuario.

## Base de datos no relacional

Una base de datos no relacional no necesita organizar toda la información mediante tablas relacionadas. Puede utilizar documentos, pares clave-valor, grafos u otras estructuras.

## ¿Cuál utilizaríamos para COINK?

Para este ejercicio se considera adecuada una base de datos relacional porque la información puede organizarse mediante entidades relacionadas como:

**Usuario → Depósito → Oink → Transacción**

Esto permite organizar los datos y consultar la información de los depósitos de los usuarios.

---

# 3.3 DIAGRAMA DE FLUJO DEL OINK

El funcionamiento general del sistema puede representarse de la siguiente manera:

```text
INICIO
   ↓
Usuario introduce la moneda
   ↓
El Oink recibe la moneda
   ↓
Se identifica y valida la moneda
   ↓
¿La moneda es válida?
   ↓
  SÍ
   ↓
Se registra el depósito
   ↓
Los datos son enviados al sistema
   ↓
Se actualiza la billetera digital
   ↓
El usuario consulta su saldo
   ↓
¿Desea retirar dinero?
   ↓
  SÍ
   ↓
Solicita el retiro
   ↓
Se verifica el saldo disponible
   ↓
Se procesa el retiro
   ↓
Se actualiza el saldo
   ↓
FIN
```

---

# 4. VIGILANCIA TECNOLÓGICA

La vigilancia tecnológica permite identificar soluciones tecnológicas relacionadas con hardware, software, bases de datos y diferentes áreas de aplicación.

Para este análisis se pueden estudiar tecnologías relacionadas con:

| Tecnología                  | Tipo                       | Relación con bases de datos             | Utilidad                                          |
| --------------------------- | -------------------------- | --------------------------------------- | ------------------------------------------------- |
| Internet de las Cosas (IoT) | Hardware y software        | Genera y almacena datos de dispositivos | Permite recopilar información automáticamente     |
| Sensores inteligentes       | Hardware                   | Generan datos que pueden almacenarse    | Permiten medir diferentes variables               |
| Computación en la nube      | Software e infraestructura | Permite almacenar y procesar datos      | Facilita el acceso remoto a la información        |
| Blockchain                  | Software                   | Utiliza registros distribuidos          | Permite registrar y verificar transacciones       |
| Inteligencia artificial     | Software                   | Utiliza grandes cantidades de datos     | Permite analizar información y generar resultados |

## Importancia

Estas tecnologías pueden trabajar junto con bases de datos para almacenar, organizar, consultar y analizar información.

En proyectos financieros, por ejemplo, los dispositivos pueden recopilar datos, enviarlos a una plataforma y almacenarlos en una base de datos para posteriormente analizarlos.

---

# 5. BASES DE DATOS EN LA NUBE

Las bases de datos pueden encontrarse en servidores locales o utilizar servicios de computación en la nube.

Para esta actividad se analizaron cinco empresas:

* AWS.
* Google Cloud.
* Microsoft Azure.
* Oracle Cloud.
* IBM Cloud.

## Tabla comparativa

| Empresa         | Servicios de bases de datos relacionales | Servicios no relacionales |
| --------------- | ---------------------------------------- | ------------------------- |
| AWS             | Amazon RDS, Amazon Aurora                | Amazon DynamoDB           |
| Google Cloud    | Cloud SQL, Cloud Spanner                 | Firestore, Bigtable       |
| Microsoft Azure | Azure SQL Database                       | Azure Cosmos DB           |
| Oracle Cloud    | Oracle Database                          | Oracle NoSQL Database     |
| IBM Cloud       | IBM Db2                                  | IBM Cloudant              |

## AWS

AWS ofrece servicios de computación en la nube para almacenar, administrar y procesar información.

Entre sus servicios de bases de datos se encuentran Amazon RDS, Amazon Aurora y Amazon DynamoDB.

## Google Cloud

Google Cloud proporciona herramientas para almacenar, consultar y analizar grandes cantidades de información.

Entre sus servicios se encuentran Cloud SQL, Cloud Spanner, Firestore y Bigtable.

## Microsoft Azure

Microsoft Azure ofrece servicios para desarrollar y administrar aplicaciones y bases de datos en la nube.

Entre sus principales servicios se encuentran Azure SQL Database y Azure Cosmos DB.

## Oracle Cloud

Oracle Cloud ofrece servicios de infraestructura y bases de datos orientados principalmente a sistemas empresariales.

Entre sus productos se encuentran Oracle Database y Oracle NoSQL Database.

## IBM Cloud

IBM Cloud ofrece servicios para almacenar y procesar información.

Entre sus soluciones se encuentran IBM Db2 y IBM Cloudant.

---

# CONCLUSIÓN

Las bases de datos son fundamentales para almacenar, organizar y analizar información.

Durante esta actividad se estudiaron diferentes conceptos relacionados con bases de datos, Internet de las Cosas, computación en la nube, análisis de datos y chatbots.

El proyecto COINK permite observar cómo un dispositivo físico puede interactuar con sistemas digitales para registrar información y actualizar una billetera digital.

También se comprendió la diferencia entre bases de datos relacionales y no relacionales, además de conocer diferentes servicios de bases de datos disponibles en la nube.

Finalmente, el desarrollo del chatbot permite aplicar conocimientos de programación, manejo de datos e inteligencia artificial en un proyecto práctico.
