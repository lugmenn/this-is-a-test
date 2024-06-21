# -*- coding: utf-8 -*-
"""Fitbit Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10CKssTGfjEIFDRH5VGvjAT01XValSdn1

Google Data Analytics Certificate

(Adaptado para Python)

**Proyecto de análisis 2/Capstone project 2**

# **Tabla de contenido**
1. [Resumen](#introduction)
2. [Definición del problema](#paragraph1)
3. [Preparación de datos](#paragraph2)

    3.1 [Conjunto de datos](#subparagraph1)

    3.2 [Origen de los datos](#subparagraph2)

    3.3 [Organización de los datos y verificación](#subparagraph3)

    3.4 [Veracidad e integridad de los datos](#subparagraph4)

4. [Procesamiento de datos (ETL)](#paragraph3)

    4.1 [Herramientas de trabajo y librerías utilizadas](#subparagraph5)

    4.2 [Importación de archivos](#subparagraph6)

    4.3 [Primer acercamiento a los datos](#subparagraph7)

    4.4 [Limpieza y transformación de datos](#subparagraph8)

5. [Análisis](#paragraph4)

    5.1 [Primer acercamiento estadístico](#subparagraph9)

    5.2 [¿Quiénes son los usuarios?](#subparagraph10)

    5.3 [Hábitos de los usuarios](#subparagraph11)

    5.4 [¿Cómo varía la actividad física durante el día?](#subparagraph12)

    5.5 [Tiempo de uso de los dispositivos](#subparagraph13)
    
6. [Conclusiones y recomendaciones](#paragraph5)

# **1. Resumen** <a name="introduction"></a>

Bellabeat es una empresa de bienestar fundada en el 2014 por Urška Sršen y Sandro Mur. Los productos de la empresa están pensados principalmente para las mujeres, enfocados en la recopilación de datos biométricos para poder ofrecer recomendaciones a quienes utilicen sus productos y que estas logren tener un impacto positivo en su salud y bienestar.

Actualmente (2024), Bellabeat tiene aproximadamente 10 millones de usuarios a nivel global, con más de 1 millón de dispositivos sincronizados.

El propósito del proyecto fue el descubrimiento de nuevas oportunidades de crecimiento para Bellabeat, logrado a través de un análisis en el uso de dispositivos similares fabricados por la competencia, apartir del cual se desarrolló la propuesta de recomendaciones que permitan aumentar el uso de los dispositivos y sus registros y al mismo tiempo, mejorar la salud de los usuarios.

# **2. Definición del problema** <a name="paragraph1"></a>

## 2.1 Tarea empresarial

**Objetivos**:


1.   Describir la manera en la que se utilizan dispositivos inteligentes similares a aquellos producidos por Bellabeat.
2.   Poder recomendar acciones para lograr un mayor acercamiento a los usuarios y la mejora y desarrollo de los productos fabricados por Bellabeat.




Este análisis estará basado en datos recopilados en relojes inteligentes de FitBit.

## 2.2 Partes interesadas /*stakeholders*

Urška Sršen: cofundadora y CPO (Directora creativa de producto) de Bellabeat
Sandro Mur: cofundador y CEO (Director ejecutivo) de Bellabeat.
Bellabeat Marketing Analytics Team / Equipo de análisis de datos de marketing.

# **3. Preparación de datos** <a name="paragraph2"></a>

## 3.1 Conjunto de datos <a name="subparagraph1"></a>

Los datos analizados provienen del registro de actividad diaria a través de diversos dispositivos inteligentes de Fitbit.
Estos datos son de dominio público (licencia CC0 1.0), obtenidos de Kaggle a través del usuario Möbius . Al ser de dominio público, los autores del conjunto de datos otorgan su permiso para que los datos recopilados también puedan ser modificados, copiados, procesados y distribuidos libremente.

## 3.2 Origen de los datos <a name="subparagraph2"></a>

El conjunto de datos original  fue recopilado por medio de una encuesta distribuida por Amazon Mechanical Turk, en donde 30 usuarios prestaron su consentimiento para el envío de datos personales de seguimiento de actividad física en minutos, ritmo cardiaco, patrones de sueño y estimado de calorías quemadas a lo largo del día. Estos datos brindan la oportunidad de conocer algunos hábitos que los usuarios podrían tener, como conductas o preferencias individuales. Las diferencias entre la manera en que se presentan algunos datos dentro de los archivos pueden deberse al uso de distintos dispositivos y configuraciones definidas por los usuarios.

## 3.3 Organización de los datos y verificación <a name="subparagraph3"></a>

Los datos recopilados consisten en información registrada de manera diaria por 30 usuarios, disponible en 18 archivos con extensión .csv, en el periodo comprendido entre marzo-12-2016 y mayo-12-2016 (dos meses).

La estructura de los datos incluye un registro por punto temporal, es decir, los archivos incluyen varios registros para un solo usuario (celdas repetidas), en donde cada registro corresponde a un día o minuto en específico. Cada usuario tiene un id único, lo cual permite la identificación individual para facilitar el procesamiento de datos y su análisis.

Las fechas para el inicio del registro no coinciden en todos los usuarios, así como el número de registros obtenidos para cada uno. Posiblemente esto se deba a la fecha en la que cada usuario aceptó participar en la recopilación de datos y que no todos los usuarios mantuvieron su registro diario o su participación en el programa.

Para un mejor entendimiento inicial de los datos, primero fueron estudiados a través de Microsoft Excel, conociendo su estructura, número total de registros y una familiarización con las variables, en donde se generaron tablas dinámicas para obtener un resumen rápido de la información disponible en cada archivo.

| ARCHIVOS (_.csv_) | DESCRIPCIÓN |
|:----------|:----------|
| dailyActivity_merged    | Registros de actividad física diaria proveniente de 33 usuarios.<br>Información agrupada para pasos, tiempo en actividad y distancia<br>recorrida. No todos los usuarios tienen el mismo número de días<br>registrados (min: 4 días, max : 31 días).   |
| dailyCalories_merged    | Registro diario de las calorías quemadas por 33 usuarios.   |
| dailyIntensities_merged    | Registro de intensidades de actividad (tiempo y distancia) diaria de<br> 33 usuarios.   |
| dailySteps_merged    | Conteo de pasos diarios de 33 usuarios.   |
| heartrate_seconds_merged    | Ritmo cardiaco de 7 usuarios registrado durante varias veces por<br> cada minuto del día.   |
| hourlyCalories_merged    | Estimado de calorías consumidas cada hora por 33 usuarios.   |
| hourlyIntensities_merged    | Total y promedio de niveles de intensidad en la actividad física<br> durante cada hora en 33 usuarios.   |
| hourlySteps_merged    | Conteo total de pasos en cada hora registrados por 33 usuarios.   |
| minuteCaloriesNarrow_merged    | Estimado de calorías consumidas cada minuto por 33 usuarios<br> (un minuto en cada fila).   |
| minuteCaloriesWide_merged    | Estimado de calorías consumidas desglosado por cada minuto de<br> cada hora por 33 usuarios (un minuto en cada columna).   |
| minutelntensitiesNarrow_merged    | Nivel de intensidad en la actividad física por minuto de 33 usuarios<br> (un minuto en cada fila).   |
| minuteIntensitiesWide_merged    | Nivel de intensidad en la actividad física, desglosado por cada <br>minuto en cada hora de 33 usuarios (un minuto en cada columna).   |
| minuteMETsNarrow_merged    | Equivalente metabólico (tasa de energía utilizada en reposo)<br> registrado por minuto en 33 usuarios.   |
| minuteSleep_merged    | Registro por minuto del sueño en 24 usuarios. No se indica la<br> unidad de medida.   |
| minuteStepsNarrow_merged    | Conteo de pasos por minuto en 33 usuarios (un minuto en cada<br> fila).   |
| minuteStepsWide_merged    | Conteo de pasos por minuto en cada hora en 33 usuarios (un minuto<br> en cada columna).   |
| sleepDay_merged    | Registro diario en 24 usuarios del tiempo total permaneciendo<br> acostado, dormido y el número de registros por día.   |
| weightLogInfo_merged    | 67 registros de peso en kg y libras durante 30 días. Cálculo de BMI.<br>Registros obtenidos de 8 usuarios, los cuales 5 lo hicieron manualmente.   |

## 3.4 Veracidad e integridad de los datos <a name="subparagraph4"></a>

El conjunto de datos proporcionado para llevar a cabo la tarea empresarial presenta diversas características que pueden representar un problema al momento de ser analizados.
En primer lugar, el tamaño de muestra, siendo pequeña, con un registro inicial de 35 usuarios, entre los cuales, no todos tienen el mismo número de días registrados (algunos con menos de diez registros), puede representar un factor de sesgo, siendo posible un análisis estadístico erróneo; así como el desconocimiento de cómo fueron recopilados éstos y de quienes provienen. Es decir, no se conoce cierta información personal y otros detalles socioeconómicos y culturales de las personas a partir de las cuáles fue obtenida la información, como el género, edad, ubicación y ocupación, entre otras características. Es por esto por lo que los resultados del análisis de los datos proporcionados realmente no podrían ser específicos para un target en el desarrollo de campañas de marketing o para conocer el comportamiento de un grupo específico de la población.

En segundo lugar, el conjunto de datos proporcionado cuenta con información recopilada durante dos meses del primer semestre del 2016, por lo que puede llegar a ser obsoleta. La última actualización del conjunto de datos y su descripción en Kaggle se realizó en marzo del 2024, sin embargo, se mantienen los registros del 2016.

Los avances tecnológicos y las nuevas necesidades han facilitado el desarrollo de nuevas funcionalidades en dispositivos inteligentes que aún no existían en ese entonces, por lo que no podrían ser estudiadas todas las maneras en las que los usuarios utilizan sus dispositivos actualmente.

Sin embargo, es posible conocer, de manera muy general, cuáles podrían ser las funcionalidades básicas más utilizadas por ciertos usuarios de dispositivos inteligentes enfocados en la salud y algunos de sus hábitos. Debido a estas razones, el presente análisis será únicamente descriptivo y enfocado en los datos suministrados.

# **4. Procesamiento de datos (ETL)** <a name="paragraph3"></a>

Debido al tamaño de los archivos, se decidió procesarlos y analizarlos a través de Python, gracias a su capacidad computacional para la ejecución de las tareas necesarias como limpieza, análisis y visualización.

##4.1 Herramienta de trabajo y librerías utilizadas <a name="subparagraph5"></a>


Primero, se procedió con la importación de las librerías que fueron utilizadas : Re, para el procesamiento de cadenas de texto (ReGex); Numpy y Pandas para el procesamiento numérico, de limpieza y manejo de la información; el paquete Stats, de SciPy para un análisis estadístico más especializado; y Matplotlib y Seaborn para la visualización de datos.
"""

import scipy.stats as stats
import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt
import seaborn as sns

# para facilitar la lectura del documento, se ocultaron los mensajes de alerta
import warnings
warnings.filterwarnings('ignore')

"""## 4.2 Importación de archivos <a name="subparagraph6"></a>

A continuación, debido al contenido de los archivos, se eligieron únicamente aquellos que se consideraron con información relevante para el enfoque en este proyecto.

Estos fueron:  

*   _dailyActivity_merged.csv_
*   _hourlySteps_merged.csv_
*   _sleepDay_merged.csv_



Los archivos "_weightLogInfo_merged.csv_" no fue considerado para el análisis debido a que únicamente cuenta con registros de 8 usuarios. Si bien el archivo "_sleepDay_merged.csv_" únicamente contiene registros de 24 usuarios y no tiene el mismo tamaño de muestra que los otros archivos (al menos 30 usuarios), se utilizó como práctica para escribir código.

La información completa de los archivos "_dailyActivity_merged.csv_" y "_hourlySteps_merged.csv_" se encuentra en dos archivos separados: el primero comprende los registros entre el 12 de marzo de 2016 y el 11 de abril de 2016, y el segundo los registros entre el 12 de abril del 2016 y el 12 de mayo del 2016.
Por lo tanto, se procedió a unificarlos en uno solo.
"""

# registros entre 12-marzo-2016 y 11-abril-2016
daily_act1 = pd.read_csv('/content/Fitbit analysis/dailyActivity_merged1.csv')

# registros entre 12-abril-2016 y 12-mayo-2016
daily_act2 = pd.read_csv('/content/Fitbit analysis/dailyActivity_merged.csv')

dailyact = pd.concat([daily_act1, daily_act2], keys= [1, 2])

# registros entre 12-marzo-2016 y 11-abril-2016
steps1 = pd.read_csv('/content/Fitbit analysis/hourlySteps_merged1.csv')

# registros entre 12-abril-2016 y 12-mayo-2016
steps2 = pd.read_csv('/content/Fitbit analysis/hourlySteps_merged.csv')

hourlysteps = pd.concat([steps1, steps2], keys= [1, 2])

# importando los registros de sueño
sleep = pd.read_csv('/content/Fitbit analysis/sleepDay_merged.csv')

"""## 4.3 Primer acercamiento a los datos <a name="subparagraph7"></a>

Para conocer la estructura, variables y tipos de datos en cada archivo se utilizaron funciones y métodos como .head(), .columns, .shape e .info().
Como resumen, los dataframes generados incluyen la siguiente información:


1.   **dailyact**: registro de actividad diaria en 35 usuarios durante hasta dos meses.
2.   **hourlysteps**: conteo de pasos de 35 usuarios durante cada hora por hasta dos meses.
3.   **sleep**: registro de sueño diario en 24 usuarios durante hasta dos meses.






"""

print(sleep.shape)
sleep.columns

sleep.info()
sleep.head()

dailyact.info()
dailyact.head()

hourlysteps.info()
hourlysteps.head()

"""## 4.4 Limpieza  y transformación de datos <a name="subparagraph8"></a>

Resultó necesaria la modificación de ciertos datos en los archivos importados, con el fin de eliminar inconsistencias entre la información disponible en cada uno y errores en el formato de algunos datos.

### 4.4.1 Eliminación de datos duplicados

Primero, se decidió verificar el numero de usuarios con registros en cada archivo, y posteriormente, en caso de contar con registros duplicados, estos fueron eliminados.
"""

print('Users in dailyact:', len(dailyact['Id'].unique()))
print('Users in hourlysteps:', len(hourlysteps['Id'].unique()))
print('Users in sleep:', len(sleep['Id'].unique()))

# encontrando el número de filas duplicadas en dailyact
dailyact_duplicate = pd.DataFrame(dailyact.duplicated())
dailyact_duplicate.iloc[:].value_counts()

# encontrando el número de filas duplicadas en hourlysteps
hourlysteps_duplicate = pd.DataFrame(hourlysteps.duplicated())
hourlysteps_duplicate.iloc[:].value_counts()

"""En el dataframe de _hourlysteps_ se encontraron 175 duplicados, por lo cual se identificaron las filas repetidas dentro del conjunto de datos y se verificó tal resultado."""

# se agregó una etiqueta a las filas duplicadas para su selección
hourlysteps['Duplicate'] = hourlysteps.duplicated()
hourlysteps[hourlysteps['Duplicate']==True]

"""En "_hourlysteps_" las 175 filas que se encontraron como duplicados, fueron generadas por un traslape de datos entre el primer y segundo archivo al contener registros de la madrugada del 12 de abril, por lo que se eliminaron del dataframe original. Al eliminar estos duplicados permanecieron 46, 008 registros."""

# se eliminó la columna 'Duplicates' debido a que las etiquetas True/False eliminaban el estatus de duplicado
hourlysteps.drop('Duplicate', inplace=True, axis =1)
#eliminando las filas duplicadas
hourlysteps.drop_duplicates(inplace=True)
# y verificando el número de datos restantes
hourlysteps.info()

"""Para el dataframe "_sleep_" se llevó a cabo el mismo procedimiento para eliminar las filas duplicadas."""

# encontrando el número de filas duplicadas en sleep
sleep_duplicate = pd.DataFrame(sleep.duplicated())
sleep_duplicate.iloc[:].value_counts()

# se agregó una etiqueta a las filas duplicadas (3 filas) para su selección y verificación
sleep['Duplicate'] = sleep.duplicated()
sleep[sleep['Duplicate']==True]

# y después fueron eliminados
sleep.drop('Duplicate', inplace=True, axis =1)
sleep.drop_duplicates(inplace=True)
sleep.info()

# reseting the index and deleting any missing values there might be
dailyact = dailyact.droplevel(0)

dailyact.dropna(inplace=True)
dailyact.info()

hourlysteps = hourlysteps.droplevel(0)
hourlysteps.dropna(inplace=True)

hourlysteps.head()

"""### 4.4.2 Filtrado de muestra

El dataframe _dailyact_ contiene la información de 35 usuarios. Sin embargo, no existe el mismo número de registros para cada usuario. para evitar la influencia de valores extremos y un sesgo durante el análisis, se realizó un conteo del número de registros existente para cada uno de los usuarios, para posteriormente ser filtrados aquellos usuarios con menos de 30 días de registro,
"""

records_by_user = dailyact.groupby('Id')['ActivityDate'].count().sort_values().to_frame('Days of use')
records_by_user.reset_index(inplace=True)
records_by_user.head()

"""Debido a que los usuarios "_2891001357_" y "_6391747486_" únicamente cuentan con 8 y 9 registros, respectivamente, fueron excluidos del análisis, con lo cual se mantuvo una muestra de 33 usuarios."""

# lista con usuarios conservados
users_to_keep = list(records_by_user['Id'][2:])
# aplicar filtro al dataframe
dailyact_filter = dailyact.loc[dailyact['Id'].isin(users_to_keep)]
dailyact_filter.reset_index(inplace=True)
print('There are', len(dailyact_filter['Id'].unique()), 'users in the "dailyact" dataframe')

hourlysteps

"""### 4.4.3 Estandarización de columnas

Para facilitar la unión de tablas para el análisis y la escritura de código, se modificaron los nombres de las columnas, eliminando las mayúsculas en los nombres de estas (uppercase-lowercase).
"""

print('1:',dailyact_filter.columns)
print('2:',hourlysteps.columns)
print('3:',sleep.columns)

cols = dailyact_filter.columns
dailyact_filter.columns = [x.lower().strip() for x in cols]
dailyact_filter.columns

cols = hourlysteps.columns
hourlysteps.columns = [x.lower().strip() for x in cols]

cols = sleep.columns
sleep.columns = [x.lower().strip() for x in cols]
sleep.head()

"""### 4.4.4 Ajustes en formato de fecha y ordenamiento de datos

Finalmente, se realizó un ajuste en las fechas incluídas en los registros, verificando que estuvieran en el formato adecuado.
"""

if pd.to_datetime(dailyact_filter['activitydate'], format='%m-%d-%Y', errors='coerce').notnull().all():
    print('The date format is ok')
else:
  print('The date format is NOT ok')

# Corroborando los valores y el formato de los datos en la columna "activitydate"
dailyact_filter['activitydate'].unique()

# después de haber verificado que los datos no se encontraban con el formato adecuado, se realizó la conversión
dailyact_filter['activitydate'] = pd.to_datetime(dailyact_filter.activitydate)
print(dailyact_filter['activitydate'])

# se corroboró que los datos fueran de tipo datetime y no un objeto de Pandas
dailyact_filter.info()

"""Para finalizar la transformación del dataframe con el registro de actividad diaria, se reordenaron los datos con base en el usuario y la fecha del registro."""

dailyact_clean = dailyact_filter.sort_values(by = ['id', 'activitydate'], ascending = [True, True], na_position = 'first', ignore_index = True)
dailyact_clean.drop('index',inplace=True, axis=1)
dailyact_clean.head()

"""Para los otros dos dataframes se realizó la misma conversión y verificación. Sumado a esto, tanto "_hourlysteps_" como "_sleep_" contaban con registro de fecha y hora, en las columnas _activityhour_ y _sleepday_, respectivamente.

Para facilitar el manejo de los datos, esta información fue separada en dos columnas distintas : en "_hourlysteps_", la información correspondiente al día fue colocada en _activitydate_ y la hora en _activitytime_; mientras que en el marco de datos "_sleep_" la información fue dividida entre las columnas _sleepday_ y _sleephour_.

Adicionalmente, para los registros del tiempo, el formato de 12 horas fue transformado a uno de 24 horas.
"""

hourlysteps['activityhour'] = pd.to_datetime(hourlysteps['activityhour'], format='%m/%d/%Y %I:%M:%S %p')
hourlysteps['activitydate'] = hourlysteps['activityhour'].dt.date
hourlysteps['activitytime'] = hourlysteps['activityhour'].dt.time
hourlysteps['activitydate'] = pd.to_datetime(hourlysteps['activitydate'], format='%m/%d/%Y')
hourlysteps.dtypes

hourlysteps = hourlysteps[['id', 'activitydate', 'activitytime', 'steptotal']]
hourlysteps.head()

sleep['sleepday'] = pd.to_datetime(sleep['sleepday'], format='%m/%d/%Y %I:%M:%S %p')
sleep['sleep_day'] = sleep['sleepday'].dt.date
sleep['sleephour'] = sleep['sleepday'].dt.time
sleep['sleepday'] = pd.to_datetime(sleep['sleep_day'], format='%m/%d/%Y')
sleep.info()

"""En el caso de las horas registradas dentro del dataframe _sleepday_, se eliminó la columna en donde se encontraba este registro, debido a que cada uno de los registros marcaba la medianoche, y en las columnas restantes, el conteo total de minutos se encuentra agrupado por día (presente en la columna "sleepday").
Por otra parte, las unidades en las columnas _totalminutesasleep_ y _totaltimeinbed_ se encuentran en minutos. Para tener una mejor comprensión del tiempo, se realizó la conversión a horas y el cambio en el nombre de las columnas (_hoursasleep_ y _hoursinbed_)
"""

sleep['sleephour'].unique()

sleep = sleep[['id', 'sleepday', 'totalsleeprecords', 'totalminutesasleep', 'totaltimeinbed']]
sleep['totalminutesasleep'] = sleep['totalminutesasleep']/60
sleep['totaltimeinbed'] = sleep['totaltimeinbed']/60
sleep.rename(columns={'totalminutesasleep':'hoursasleep', 'totaltimeinbed':'hoursinbed' }, inplace=True)
sleep.head()

"""Por último, para estudiar las correlaciones entre algunas variables del registro de actividad y las características del sueño en algunos de los usuarios, se unificaron los dataframes "_dailyact_clean_" y "_sleep_", utilizando como llaves el id y la fecha del registro. Al haberse realizado un _inner join_, este marco de datos únicamente contiene la información de los 24 usuarios que realizaron el registro del sueño."""

# reemplazo del nombre de una columna para la unificación de tablas
sleep.rename(columns={'sleepday':'activitydate'}, inplace=True)

act_sleep = pd.merge(dailyact_clean, sleep,
                     how='inner', on= ['id', 'activitydate'])

act_sleep.head()

"""Con esto, se encuentran listos cuatro marcos de datos, o dataframes listos para el análisis:


1.   dailyact_clean
2.   hourlysteps
3.   act_sleep
4.   sleep

# **5. Análisis** <a name="paragraph4"></a>

## 5.1 Primer acercamiento estadístico <a name="subparagraph9"></a>

Se utilizó la función _describe()_ en cada marco de datos para tener un resumen de los valores presentes en cada uno, con la finalidad de encontrar alguna ruta a seguir para los análisis posteriores.
"""

# configurando el estilo de las gráficas que serán generadas a través de matplotlib y seaborn
sns.set_context("paper")
sns.set_theme('paper')
sns.set_style('whitegrid')

dailyact_summary = dailyact_clean.describe().drop(['id','activitydate'], axis=1)
dailyact_summary

"""Generando una primera gráfica, fue posible observar que en los registros sí existe una relación directa entre la cantidad total de pasos, la distancia recorrida y las calorías consumidas por cada usuario. Esto fue de utilidad para poder clasificar a los usuarios en distintas categorías de acuerdo a su nivel de actividad."""

sns.relplot(data = dailyact_clean, x = 'totalsteps', y = 'calories', hue = 'totaldistance').set_xticklabels(rotation=45)

sns.lmplot(data = dailyact_clean,
           x = 'totalsteps',
           y = 'calories',
           lowess=True,
           scatter_kws={'alpha':0.3, "color": "#daa2ab"},
           line_kws={'color': '#945685'}).set_xticklabels(rotation=45)

hourlysteps_summary = hourlysteps.describe().drop(['id','activitydate'], axis=1)
hourlysteps_summary

sleep_summary = sleep.describe().drop(['id','activitydate'], axis=1)
sleep_summary

"""## 5.2 ¿Quiénes son los usuarios? <a name="subparagraph10"></a>

Para llevar a cabo un análisis basado en las clases de usuarios de los dispositivos inteligentes de acuerdo a sus niveles de actividad, se determinaron 4 clases de usuarios con base en la clasificación propuesta por Tudor-Locke & Bassett, 2004, et. al. en su artículo "_How many steps/day are enough? Preliminary pedometer indices for public health_" (https://pubmed.ncbi.nlm.nih.gov/14715035/)



*   Sedentary/Sedentario : pasos al día < 5000
*   Low active/Poco activo : 5000 <= pasos al día < 7499
*   Fairly active/Moderadamente activo : 7500 <= pasos al día < 9999
*   Active/Muy activo : 10 000 < pasos al día



Con esta clasificación, se obtuvo el promedio de los pasos al día registrados y le fue asignado a cada usuario una categoría. Después, se calculó el porcentaje del tipo de usuarios para comprender de mejor manera qué tipo de usuarios utilizan estos dispositivos inteligentes enfocados en la salud.






"""

# cálculo del promedio diario de pasos y calorias consumidas por cada usuario
avgact = dailyact_clean.groupby('id').agg({'totalsteps': np.nanmean,'calories': np.nanmean})
avgact.rename(columns={'totalsteps':'avgsteps','calories':'avgcalories'}, inplace=True)
avgact.head()

# definición de función para asignar categorías

def user_type(steps):
  if steps < 5000:
    return "Sedentary"
  elif (steps>=5000) & (steps<7499):
    return "Lightly Active"
  elif (steps>=7500) & (steps<9999):
    return "Fairly Active"
  else:
    return "Active"

# iteración de la función sobre los datos
avgact['activity_level'] = avgact['avgsteps'].apply(lambda x: user_type(x))
avgact.head()

# cálculo del porcentaje de usuarios

types_ofuser = avgact.groupby('activity_level')['avgsteps'].count().to_frame('no. of users')
totalusers = types_ofuser['no. of users'].sum()
types_ofuser['user percentage'] = types_ofuser['no. of users']/totalusers
types_ofuser

sns.set_style('whitegrid')
sns.catplot(data = types_ofuser, x = 'activity_level', y= 'no. of users', kind = 'bar', color='#945685')

colors = sns.cubehelix_palette(hue=1)
sns.set_style('whitegrid')
plt.figure(figsize=(6,6))
plt.pie(types_ofuser['user percentage'],
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops = {'linewidth': 4},
        center = (0.1,0.1))
plt.legend(title='User type percentage',
           bbox_to_anchor=(1.0, 0.6),
           loc='upper left', borderaxespad=0,
           labels = types_ofuser.index)
plt.title('How active are the users?', size=12)
plt.show()

"""## 5.3 Hábitos de los usuarios <a name="subparagraph11"></a>

A partir del marco de datos _act_sleep_ se encontró la relación entre el promedio de pasos y las horas de sueño a lo largo de la semana (cantidad por día) para poder tener una idea general de cuándo tienen un mayor uso los dispositivos inteligentes y si los usuarios cumplen con las horas de sueño recomendadas por la OMS.
"""

act_sleep['weekday'] = act_sleep['activitydate'].dt.day_name()
act_sleep.head()

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
daily_sleep = act_sleep.groupby('weekday').agg({'totalsteps': np.nanmean, 'hoursasleep' : np.nanmean}).reindex(days)
daily_sleep.rename(columns={'totalsteps':'avgsteps', 'hoursasleep': 'avg_hoursasleep'},inplace=True)
daily_sleep

fig, axes = plt.subplots(1, 2, sharex=True, figsize=(7,5))
fig.suptitle("Daily users' habits")
axes[0].set_title('Average steps per day')
axes[1].set_title('Average hours of sleep per day')
sns.barplot(ax=axes[0], x=daily_sleep.index, y=daily_sleep['avgsteps'], color='#daa2ab')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)
sns.barplot(ax=axes[1], x=daily_sleep.index, y=daily_sleep['avg_hoursasleep'], color='#5f3867')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)
axes[0].axhline(y=7500, linewidth=1, color='black', ls='--')
axes[1].axhline(y=7, linewidth=1, color='black', ls='--')
#sns.catplot(data = daily_sleep, x = daily_sleep.index, y= 'avgsteps', kind = 'bar')

"""La Organización Mundial de la Salud recomienda, en adultos, entre 7 y 9 horas de sueño al día. Tomando esto como referencia, fue posible observar que, en promedio, la cantidad recomendada no es alcanzada la mayoría de los días, siendo el domingo el día en el que los usuarios registraron mayores horas de sueño.

Esto coincidió con la actividad registrada, en donde el domingo presentó la menor cantidad de pasos, con una actividad física ligera, por debajo de los 7500 pasos, de acuerdo a las categorías designadas anteriormente, y el único día por debajo del promedio diario calculado a partir de la muestra, que fue de 7357 pasos.

Para tener mayor certeza y saber si la cantidad de pasos o actividad física tiene una relación con las horas de sueño en los usuarios, se realizó el cálculo de la Correlación de Pearson entre ambas variables.
"""

# ¿existe una relación entre la actividad física y la cantidad de horas de sueño en el mismo día?

def sleep_stepscorr():
  corr, pval = stats.pearsonr(act_sleep["totalsteps"],act_sleep["hoursasleep"])
  return print('cor=', corr, 'P-value=', pval)

# Coeficiente de Correlación de Pearson
sleep_stepscorr()

"""Utilizando un análisis de correlación de Pearson, fue posible apreciar que el coeficiente de correlación tiene un valor negativo (con un valor de -0.19). Sin embargo, este no indica que haya una fuerte relación entre las dos variable.Si bien se obtuvo un valor p(<0.05) cercano a 0, es posble que también un sesgo en los resultados debido a los valores extremos que se pueden visualizar en la gráfica de la regresión local de Lowess."""

sns.lmplot(data = act_sleep,
           x = 'totalsteps',
           y = 'hoursasleep',
           lowess=True,
           scatter_kws={'alpha':0.3, "color": "#daa2ab"},
           line_kws={'color': '#945685'}).set_xticklabels(rotation=45)

"""## 5.4 ¿Cómo varía la actividad física durante el día? <a name="subparagraph12"></a>

Para comprender de mejor manera la actividad física diaria, también se procesó la información para conocer cuáles fueron los momentos del día en los que los usuarios fueron más activos.
"""

stepsperhour = hourlysteps.groupby('activitytime')['steptotal'].mean().to_frame()
stepsperhour.rename(columns={'steptotal':'avg steps'}, inplace=True)
stepsperhour.head()

sns.set_context("paper")
sns.set_theme('paper')
sns.set_style('whitegrid')
plt.figure(figsize=(9,5))
pal = sns.color_palette("rocket", 24)
rank = stepsperhour['avg steps'].argsort().argsort()  # http://stackoverflow.com/a/6266510/1628638
ax=sns.barplot(x = stepsperhour.index, y = stepsperhour['avg steps'], palette=np.array(pal[::-1])[rank])
plt.xticks(rotation=90)
ax.set(xlabel='Time of day', ylabel='Average steps')
plt.title('Average steps throughout the day')
plt.show()



"""A partir de la gráfica se pudo observar que los usuarios fueron activos principalmente en la tarde, con más de 500 pasos por hora, con dos picos de actividad: uno al medio día y el otro al atardecer. Dichos puntos en el día pudieron haber coincidido con las actividades usuales de cierto ritmo de vida, como lo podría ser la hora de la comida y la salida de los trabajos o la actividad física por la tarde.

## 5.5 Tiempo de uso de los dispositivos inteligentes <a name="subparagraph13"></a>

Para poder planear estrategias de marketing o mejorar el acercamiento entre la empresa y los usuarios, resultó conveniente evaluar cuánto tiempo aproximado son utilizados los dispositivos de este tipo por día.

Para esto, se decidió obtener la proporción del día en el usuario utilizó su dispositivo a partir del tiempo total en que se registró actividad, con base en los campos _veryactiveminutes_, _fairlyactiveminutes_, _lightlyactiveminutes_ y _sedentaryminutes_. Debido a que los dispositivos también registran momentos de inactividad, si el registro no es del 100% dentro de un período de 24 horas (1440 minutos), se puede deducir que el dispositivo no fue utilizado durante la totalidad del día.
"""

dailyact_clean['minutes used'] = dailyact_clean['veryactiveminutes'] + dailyact_clean['fairlyactiveminutes'] + dailyact_clean['lightlyactiveminutes'] + dailyact_clean['sedentaryminutes']
dailyact_clean['daily usage ratio'] = dailyact_clean['minutes used']/1440
dailyact_clean.head()

"""Este cálculó permitió la asignación de más categorías para los usuarios, que permitió hacer distinciones dentro de la muestra. Los usuarios fueron clasificados nuevamente de acuerdo al tiempo de uso de los dispositivos.


| CATEGORÍA | VALOR |
|:----------|:----------|
| All day/Todo el día    | _daily usage ratio_ = 1   |
| Over half day/Más de la mitad del día    | 1 > _daily usage ratio_ >= 0.5   |
| Less than half/Menos de la mitad del día    | 0.5 > _daily usage ratio_   |
"""

def daily_usage(ratio):
  if ratio == 1:
    return "All day"
  elif (ratio >= 0.5) & (ratio < 1):
    return "Over half day"
  else:
    return "Less than half day"

dailyact_clean['worn']= dailyact_clean['daily usage ratio'].apply(lambda x: daily_usage(x))
dailyact_clean.iloc[:5, [0,1,-3,-2,-1]]

usagerate = dailyact_clean.groupby('worn')['id'].count().to_frame()
usagerate.rename(columns={'id':'total days'},inplace=True)
usagerate['total percentage'] = usagerate['total days']/usagerate['total days'].sum()
usagerate

colors = sns.cubehelix_palette(hue=1)
sns.set_style('whitegrid')
plt.figure(figsize=(6,6))
plt.pie(usagerate['total percentage'],
        colors=colors[1:4],
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops = {'linewidth': 4},
        center = (0.1,0.1),
        pctdistance=0.85,)
plt.legend(title='Daily use of devices',
           bbox_to_anchor=(1.0, 0.6),
           loc='upper left', borderaxespad=0,
           labels = usagerate.index)
plt.title('How much were the devices worn?', size=12)
plt.show()

"""La mayoría de los usuarios de este tipo de dispositivos inteligentes le dio un uso durante todo el día, pues se obtuvo que de los 1380 registros, 696 corresponden a esta categoría, siendo un 50.43% de la muestra. Por otro lado, el 45.7% corresponde a aquellos días en los que los dispositivos fueron utilizados durante al menos más de la mitad del día. Esto permite suponer que las usuarios de los dispositivos sí les dan un gran uso día a día, aprovechando las características y funcionalidades para el registro de gran parte de sus actividades, si no es que de todas.

# 6. Conclusiones y recomendaciones <a name="paragraph5"></a>

Bellabeat es una empresa comprometida para el desarrollo de productos que permitan a sus usuarios conocerse a sí mismos y que facilite la mejora de la salud propia.

El estudio y el análisis realizado tuvo la finalidad de extrapolar los resultados para conocer la manera en la que las personas utilizan cierto tipo de productos, el tipo de personas que los utilizan y tener un mejor conocimiento de algunos de los hábitos que éstas tienen.

Esto permitió el desarrollo de propuestas que Bellabeat podría implementar para el desarrollo de sus productos y mejorar o desarrollar algunas acciones que permita un mejor acercamiento a los usuarios, de manera que sus productos sigan siendo utilizados y potencialmente, el aumento en el número de usuarios que en el futuro los puedan encontrar como una herramienta atractiva.

Las recomendaciones son:

| RECOMENDACIÓN | DESCRIPCIÓN |
|:----------|:----------|
| 1. Sistema de notificaciones<br> y mensajes     | En el análisis se observó que la mayoría de los usuarios no son sendentarios.<br> Sin embargo, para la mejora de salud, es conveniente el desarrollo de un **sistema<br> de alertas diarias para alcanzar, al menos, 7500 pasos**, de manera que los usuarios<br> sean moderamente activos **o que este sistema se personalice de acuerdo a los<br> objetivos de cada persona**. Adicionalmente, se propone el **desarrollo de mensajes<br> en dentro de la app o pop-ups en el dispositivo sobre los beneficios de aumentar**<br>**el nivel de actividad física**.  |
| 2. Alertas y recomendaciones<br> para mejorar el sueño     | También fue posible identificar que los usuarios no cumplen con el mínimo de horas<br> de sueño recomendadas por la OMS la mayoría de los días. Para la mejora en el<br> tiempo y la calidad del sueño, sería apropiado enviar **notificaciones que sugieran**<br> **al usuario prepararse para dormir de acuerdo a la configuración personal de una hora**<br> **estimada para ir a la cama**. Adicionalmente, sería útil la **divulgación de hábitos para**<br> **mejorar la calidad del sueño.**   |
| 3. Sistema de recompensas     | Para mantener un registro continuo en los usuarios y mejorar la recopilación de datos<br> para el futuro desarrollo de nuevas características, el desarrollo de un **sistema de** <br>**puntos y niveles de acuerdo de acuerdo la actividad física y el registro manual y**<br> **automático de información diariamente** podría ser de gran ayuda. Estos niveles y puntos<br> podrían ser cambiados por descuentos o planes premium dentro de los servicios y <br> productos ofrecidos por Bellabeat.    |
"""