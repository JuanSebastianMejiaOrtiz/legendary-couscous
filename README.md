# Proyecto 4 Metodos Numericos, Solucion de Ecuaciones Diferenciales

## Informacion importan

- Autor: Juan Sebastian Mejia Ortiz
- Universidad de Antioquia
- Link al cuaderno de google colab: https://colab.research.google.com/drive/182EqpUQ3QAy3obexD1JRWK5PE65Ei3V7?usp=sharing

## Sobre el proyecto

En el proyecto se solucionan dos ecuaciones diferenciales que modelan el comportamiento de un pendulo.
Se hace el analisis sin y con friccion del aire y se grafican los resultados obtenidos.

## Ecuaciones Diferenciales

### Sin Friccion

$$
\begin{aligned}
\frac{d \theta}{dt} &= \omega \\
\frac{d \omega}{dt} &= -\frac{g}{L}sin\theta
\end{aligned}
$$

### Con Friccion

$$
\begin{aligned}
\frac{d \theta}{dt} &= \omega \\
\frac{d \omega}{dt} &= -\frac{g}{L}sin\theta - \frac{c}{Lm^2}\omega
\end{aligned}
$$

## Versiones de librerias utilizadas

El programa fue probado en una Raspberry Pi 4 de 8GB utilizando el siguiente software en las versiones que se mencionan a continuacion:

- Bash 5.2.15
- Python 3.11.2
- Numpy 1.24.2
- Matplotlib 3.6.3
- Pandas 1.5.3
- Scipy 1.10.1
