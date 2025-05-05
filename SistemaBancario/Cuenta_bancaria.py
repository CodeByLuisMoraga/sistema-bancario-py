import json
import os

# Clase que modela una cuenta bancaria con atributos privados y métodos para operaciones básicas.
class CuentaBancaria:
    def __init__(self, nombre, clave="", correo="", telefono="", saldo_inicial=0):
        self.__nombre = nombre
        self.__clave = clave
        self.__correo = correo
        self.__telefono = telefono
        self.__saldo = saldo_inicial
        self.__transacciones = []

    # Propiedades para acceder a los atributos privados
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    @property
    def clave(self):
        return self.__clave

    # Método de clase para validar saldo inicial y crear un objeto CuentaBancaria
    @classmethod
    def crear_con_validacion(cls, nombre, clave, correo, telefono, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        return cls(nombre, clave, correo, telefono, saldo_inicial)

    # Método para depositar dinero a la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self.__transacciones.append(f"Depósito: {cantidad}")
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self.__transacciones.append(f"Retiro: {cantidad}")
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad inválida o saldo insuficiente.")

    # Muestra el saldo actual de la cuenta
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

    # Muestra todas las transacciones realizadas en la cuenta
    def mostrar_transacciones(self):
        print("Transacciones realizadas:")
        if self.__transacciones:
            for t in self.__transacciones:
                print(t)
        else:
            print("No hay transacciones registradas.")

# ------------------------------
# Funciones para guardar y cargar datos desde archivo JSON
# ------------------------------

# Guarda todas las cuentas en un archivo JSON
def guardar_datos(usuarios):
    datos = {}
    for nombre, cuenta in usuarios.items():
        datos[nombre] = {
            "clave": cuenta.clave,
            "correo": cuenta.correo,
            "telefono": cuenta.telefono,
            "saldo": cuenta._CuentaBancaria__saldo  # Se accede al saldo directamente desde el atributo privado
        }
    try:
        with open("datos_banco.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
        print("✅ Datos guardados correctamente.")
    except Exception as e:
        print("❌ Error al guardar datos:", e)

# Carga las cuentas desde el archivo JSON (si existe)
def cargar_datos():
    if not os.path.exists("datos_banco.json"):
        print("📁 Archivo de datos no encontrado. Se creará uno nuevo al guardar.")
        return {}
    try:
        with open("datos_banco.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
            usuarios = {}
            for nombre, info in datos.items():
                usuarios[nombre] = CuentaBancaria(
                    nombre,
                    clave=info.get("clave", ""),
                    correo=info.get("correo", ""),
                    telefono=info.get("telefono", ""),
                    saldo_inicial=info.get("saldo", 0)
                )
            print("📂 Datos cargados correctamente.")
            return usuarios
    except Exception as e:
        print("❌ Error al cargar datos:", e)
        return {}

# ------------------------------
# Menú principal de la aplicación
# ------------------------------

# Cargamos las cuentas bancarias existentes al iniciar el programa
usuarios = cargar_datos()

print("🏦 Bienvenido a su banco")
while True:
    # Menú de opciones principales
    opcion = input("\n1. Registrar\n2. Iniciar sesión\n3. Salir\nElige una opción: ")

    if opcion == "1":
        # Registro de nuevo usuario
        nombre = input("Crea tu nombre de usuario: ")
        if nombre in usuarios:
            print("⚠️ Ese usuario ya existe.")
            continue
        clave = input("Crea tu contraseña: ")
        correo = input("Ingresa tu correo electrónico: ")
        telefono = input("Ingresa tu número de teléfono: ")
        try:
            saldo_inicial = float(input("Ingresa tu saldo inicial: "))
        except ValueError:
            print("❌ Saldo inválido. Debe ser un número.")
            continue

        try:
            nuevo_usuario = CuentaBancaria.crear_con_validacion(nombre, clave, correo, telefono, saldo_inicial)
            usuarios[nombre] = nuevo_usuario
            guardar_datos(usuarios)
            print("✅ Usuario creado exitosamente.")
        except ValueError as e:
            print(f"❌ {e}")

    elif opcion == "2":
        # Ingreso de usuario existente
        nombre = input("Ingresa tu nombre de usuario: ")
        clave = input("Ingresa tu contraseña: ")
        if nombre in usuarios and usuarios[nombre].clave == clave:
            cuenta = usuarios[nombre]
            print(f"\n🔐 Bienvenido, {cuenta.nombre}")
            print(f"📧 Correo: {cuenta.correo}")
            print(f"📞 Teléfono: {cuenta.telefono}")
            # Submenú para operaciones bancarias
            while True:
                accion = input("\n1. Depositar\n2. Retirar\n3. Ver saldo\n4. Ver transacciones\n5. Cerrar sesión\nElige una opción: ")
                if accion == "1":
                    try:
                        monto = float(input("Monto a depositar: "))
                        cuenta.depositar(monto)
                    except ValueError:
                        print("❌ Monto inválido.")
                elif accion == "2":
                    try:
                        monto = float(input("Monto a retirar: "))
                        cuenta.retirar(monto)
                    except ValueError:
                        print("❌ Monto inválido.")
                elif accion == "3":
                    cuenta.mostrar_saldo()
                elif accion == "4":
                    cuenta.mostrar_transacciones()
                elif accion == "5":
                    print("🔒 Sesión cerrada.")
                    break
                else:
                    print("❌ Opción inválida.")
        else:
            print("❌ Usuario o clave incorrectos.")

    elif opcion == "3":
        # Guardar datos antes de salir
        guardar_datos(usuarios)
        print("👋 ¡Gracias por usar el banco!")
        break

    else:
        print("❌ Opción inválida.")
