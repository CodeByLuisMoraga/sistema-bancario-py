import json
import os

# Ruta al archivo JSON
ruta_archivo = "datos_banco.json"

# Verificar si el archivo existe
if os.path.exists(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if datos:
        print("📄 Usuarios registrados:\n")
        for usuario, info in datos.items():
            print(f"👤 Usuario: {usuario}")
            print(f"   📧 Correo:   {info.get('correo', 'N/A')}")
            print(f"   📞 Teléfono: {info.get('telefono', 'N/A')}")
            print(f"   🔒 Clave:    {info.get('clave', 'N/A')}")
            print(f"   💰 Saldo:    {info.get('saldo', 0)}")
            print("-" * 40)
    else:
        print("⚠️ El archivo está vacío.")
else:
    print("❌ El archivo no existe.")