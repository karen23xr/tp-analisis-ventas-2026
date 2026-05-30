"""
Script de Análisis de Datos de Ventas
TP 2 Organización Empresarial - UTN 2026
Escenario B
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Verificar/carpeta estructura
os.makedirs('datos', exist_ok=True)
os.makedirs('scripts', exist_ok=True)
os.makedirs('resultados', exist_ok=True)

# Crear datos de prueba (simulan ventas comerciales)
datos = {
    'fecha': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-10'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Mouse', 'Auriculares'],
    'cantidad': [1, 2, 1, 3, 2, 1, 5],
    'precio_unitario': [50000, 2500, 4500, 50000, 12000, 2500, 3000]
}
df = pd.DataFrame(datos)
df.to_csv('datos/ventas.csv', index=False)

# Análisis: Calcular venta total por registro
df['venta_total'] = df['cantidad'] * df['precio_unitario']

# Indicadores clave
ventas_totales = df['venta_total'].sum()
producto_estrella = df.groupby('producto')['cantidad'].sum().idxmax()
ventas_mensuales = df.groupby(pd.to_datetime(df['fecha']).dt.to_period('M'))['venta_total'].sum()

print("=== INDICADORES ===")
print(f"Ventas Totales: ${ventas_totales:,}")
print(f"Producto Más Vendido: {producto_estrella}")

# Gráfico de evolució mensual
plt.figure(figsize=(10, 6))
ventas_mensuales.plot(kind='bar', color='#2E86AB', alpha=0.8)
plt.title('Evolución de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png', dpi=150)
print("Gráfico guardado en resultados/")
