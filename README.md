# **AMBIENTES VIRTUALES**

#### Autora: **Aslhy Casteblanco**
#### Versión de Python utilizada: `Python 3.13.5`

---

## **Descripción general**

Este repositorio contiene dos proyectos desarrollados como parte del ejercicio de **ambientes virtuales en Python**, donde cada uno cuenta con su propio entorno virtual, paquetes específicos y archivos requeridos.
El objetivo es demostrar el uso correcto de **entornos virtuales, requirements.txt, scripts y notebooks.**

---
## **Estructura del repositorio**

```
AMBIENTES_VIRTUALES/
│
├── proyecto_A/
│   ├── venv_1/ (no se sube)
│   ├── algoritmo_a.py
│   ├── notebook_a.ipynb
│   ├── requirements.txt
│
└── proyecto_B/
    ├── venv_2/ (no se sube)
    ├── algoritmo_b1.py
    ├── algoritmo_b2.py
    ├── requirements.txt
```

---

## **Detalles de cada proyecto**

### **1. Proyecto A**

* **Entorno virtual:** `venv_1`

  ![Imagen de WhatsApp 2025-10-28 a las 12 48 23_7d661975](https://github.com/user-attachments/assets/362a3db4-64ab-43f6-8814-3ac8e776ea9c)
  _Creación del entorno virtual_

* **Paquete instalado:** `jupyter`
  
  ![Imagen de WhatsApp 2025-10-28 a las 12 48 49_86b9ffc0](https://github.com/user-attachments/assets/4aca2551-fec6-4403-85a6-c6c9958932ea)
  _Instalación de Jupyter_
  <br><br>
  ![Imagen de WhatsApp 2025-10-28 a las 12 49 46_40b95290](https://github.com/user-attachments/assets/e998b64c-5ced-474e-9af1-b8b7ed1f913c)
  _Activación del entorno venv_1_

* **Archivos:**

  * `algoritmo_a.py`: Calcula el promedio de una lista de números.
    
    ![Imagen de WhatsApp 2025-10-28 a las 12 51 03_cc341e48](https://github.com/user-attachments/assets/238c32a4-e366-465b-8a56-580a097826c5)

  * `notebook_a.ipynb`: Calcula el promedio de notas de varios estudiantes y mostramos un gráfico de barras con los resultados.

    ![Imagen de WhatsApp 2025-10-28 a las 12 51 30_54a6196d](https://github.com/user-attachments/assets/238823c4-7650-4093-87f7-96ec99035fcc)
    ![Imagen de WhatsApp 2025-10-28 a las 12 51 36_c0b16c93](https://github.com/user-attachments/assets/cd280e51-263f-47d2-8336-958f6ede11d8)

    _Para el diagrama de barras en el notebook con jupyter se instaló una librería, matplotlib_
    ![Imagen de WhatsApp 2025-10-28 a las 12 53 35_f6bc5ecd](https://github.com/user-attachments/assets/9673f144-cde5-4b3c-9e51-181a5a73b769)



* **Archivo `requirements.txt`** generado con:

  ```bash
  pip freeze > requirements.txt
  ```
  ![Imagen de WhatsApp 2025-10-28 a las 12 54 24_9919dcf4](https://github.com/user-attachments/assets/71bc5a2b-ecea-4a52-a147-686dadc4788f)
  
---

### **2. Proyecto B**

* **Entorno virtual:** `venv_2`
* **Paquete instalado:** `pandas`
  
  ![Imagen de WhatsApp 2025-10-28 a las 18 18 51_7f147a05](https://github.com/user-attachments/assets/7be71571-6e46-41f5-8dea-fef63b5f23ac)
  _Creación del entorno virtual e instalación de Pandas_

* **Archivos:**

  * `algoritmo_b1.py`: lee una lista de datos y calcula promedio, máximo o mínimo.
    
    <img width="1237" height="1104" alt="image" src="https://github.com/user-attachments/assets/27f57da5-65b1-4392-82ef-4305f294c1e5" />

  * `algoritmo_b2.py`: crea un DataFrame y realiza operaciones simples (sumas, filtros, etc.).

    <img width="1443" height="1085" alt="image" src="https://github.com/user-attachments/assets/8054b021-a3a1-4fed-8da8-0287b80c4301" />

* **Archivo `requirements.txt`** generado con:
  ```bash
  pip freeze > requirements.txt
  ```
  <img width="1919" height="674" alt="image" src="https://github.com/user-attachments/assets/6ccc888d-575c-42ce-b548-f7b17582027f" />

---

## Estructura de carpetas
<img width="396" height="451" alt="image" src="https://github.com/user-attachments/assets/b34febc5-1a87-42ee-a071-3807805de1a6" />

---

## **Repositorio en GitHub**
-> [https://github.com/aslhyy/AMBIENTES_VIRTUALES](https://github.com/aslhyy/AMBIENTES_VIRTUALES)

---

## **Conclusión**

Este ejercicio demuestra el uso correcto de **entornos virtuales, manejo de dependencias y control de versiones** en Python.

