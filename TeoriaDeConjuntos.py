#!/usr/bin/env python
# coding: utf-8

# # TEORÍA DE CONJUNTOS
# La teoría de conjuntos es un área fundamental de las matemáticas que trata sobre las propiedades y relaciones entre conjuntos, que son colecciones bien definidas de objetos. Python, como un lenguaje de programación versátil, ofrece varias formas de trabajar con conjuntos y aplicar conceptos de teoría de conjuntos.

# ## Creación de conjuntos
# 

# In[1]:


lista = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}


# In[2]:


lista


# In[3]:


conjunto = set(lista)


# In[4]:


conjunto


# ## Operaciones

# ## → Union
# La unión de dos conjuntos devuelve un conjunto que contiene todos los elementos que están en al menos uno de los conjuntos.Ejemplo: Si A = {1, 2, 3, 4} y B = {3, 4, 5, 6}, entonces la unión de A y B sería {1, 2, 3, 4, 5, 6}.
#                                      La fórmula para la unión de dos conjuntos es: A U B

# In[5]:


# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión de conjuntos
union = A.union(B)
print("Unión:", union)  # Salida: {1, 2, 3, 4, 5, 6}


# ## → Intersección
# La intersección de dos conjuntos devuelve un conjunto que contiene solo los elementos que están presentes en ambos conjuntos. Ejemplo: Si A = {1, 2, 3, 4} y B = {3, 4, 5, 6}, entonces la intersección de A y B sería {3, 4}. La fórmula es: A ∩ B

# In[6]:


# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Intersección de conjuntos
interseccion = A.intersection(B)
print("Intersección:", interseccion)  # Salida: {3, 4}


# ## → Diferencia
# La diferencia de dos conjuntos devuelve un conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo.
# Ejemplo: Si A = {1, 2, 3, 4} y B = {3, 4, 5, 6}, entonces la diferencia de A - B sería {1, 2} y la diferencia de B - A sería {5, 6}. Su fórmula es: A − B

# In[7]:


# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Diferencia de conjuntos
diferencia_A_B = A.difference(B)
print("Diferencia A - B:", diferencia_A_B)  # Salida: {1, 2}

diferencia_B_A = B.difference(A)
print("Diferencia B - A:", diferencia_B_A)  # Salida: {5, 6}


# ## → Diferencia simétrica
# La diferencia simétrica de dos conjuntos devuelve un conjunto que contiene los elementos que están en uno de los conjuntos pero no en ambos.
# Ejemplo: Si A = {1, 2, 3, 4} y B = {3, 4, 5, 6}, entonces la diferencia simétrica de A y B sería {1, 2, 5, 6}.
# Su fórmula es: A △ B, lo que equivale a: (A − B) ∪ (B − A)

# In[8]:


# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Diferencia simétrica de conjuntos
diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia Simétrica:", diferencia_simetrica)  # Salida: {1, 2, 5, 6}


# ## ¿Cómo realizar diagramas de Venn?
# Los diagramas de Venn son una forma visual y efectiva de representar las relaciones entre conjuntos. A continuación se explica como se pueden realizar en python utilizando la biblioteca Matplotlib. Primero, se instala la biblioteca con el siguiente comando:

# In[9]:


pip install matplotlib


# ### Importante
# Si estás utilizando Anaconda, puede ser que necesites instalar el paquete matplotlib-venn. Puedes hacerlo fácilmente utilizando el siguiente comando en tu terminal o en el Anaconda con el prompt: conda install -c conda-forge matplotlib-venn
# 
# Con eso podremos realizar un código para generar un diagrama de Venn:

# In[10]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Crear diagrama de Venn
venn2([A, B], ('A', 'B'))

# Mostrar el diagrama
plt.title("Diagrama de Venn con 2 conjuntos")
plt.show()


# ## ¿Y si quiero 3 conjuntos?
# Para hacer un diagrama de Venn con tres conjuntos en Python utilizando Matplotlib, puedes utilizar la función venn3 del módulo matplotlib_venn:

# In[11]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definición de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

# Crear diagrama de Venn
venn3([A, B, C], ('A', 'B', 'C'))

# Mostrar el diagrama
plt.title("Diagrama de Venn con 3 conjuntos")
plt.show()


# In[ ]:




