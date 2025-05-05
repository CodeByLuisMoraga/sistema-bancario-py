# 💻 Sistema Bancario en Python

Este proyecto implementa un sistema bancario simple en Python que permite realizar operaciones básicas como:

- Registro de nuevos usuarios  
- Inicio de sesión  
- Depósito y retiro de dinero  
- Consulta de saldo  
- Consulta de transacciones  

El sistema guarda y carga datos utilizando un archivo `datos_banco.json` para almacenar la información de las cuentas bancarias, permitiendo la persistencia de datos entre ejecuciones.

## ⚙️ Funcionalidades

- **Registro de usuario**: Crea una nueva cuenta con nombre de usuario, contraseña, correo electrónico, teléfono y saldo inicial.  
- **Inicio de sesión**: Verificación de credenciales para acceder al sistema.  
- **Operaciones bancarias**:
  - Depositar dinero
  - Retirar dinero (con validación de saldo insuficiente)
  - Consultar saldo
  - Consultar historial de transacciones
- **Persistencia de datos**: Toda la información se guarda en el archivo `datos_banco.json`.

## 📁 Estructura del Proyecto

- `CuentaBancaria`: Clase principal con métodos para operaciones bancarias.
- `guardar_datos()`: Guarda los datos actualizados en el archivo JSON.
- `cargar_datos()`: Carga los datos existentes al iniciar el sistema.

## 🚀 Cómo usar

### 1. Clonar el repositorio

```bash
git clone https://github.com/CodeByLuisMoraga/sistema-bancario-py.git
cd sistema-bancario-py
