import json
import random
import datetime

def generate_devices_json(num_entries=5, filename="devices.json"):
    """
    Genera un archivo JSON con 'num_entries' dispositivos de ejemplo con valores dentro de rangos específicos.
    
    :param num_entries: Cantidad de dispositivos a generar.
    :param filename: Nombre del archivo JSON que se creará o sobreescribirá.
    """
    
    device_types = ["temperature", "pressure", "speed"]
    device_status = ["active", "inactive"]
    
    value_ranges = {
        "temperature": (-10.0, 100.0),
        "pressure": (0.0, 500.0),
        "speed": (0.0, 150.0)
    }
    
    devices = []
    
    for i in range(1, num_entries + 1):
        device_type = random.choice(device_types)
        value_range = value_ranges[device_type]
        
        device = {
            "id": i,
            "name": f"Device {i}",
            "type": device_type,
            "status": random.choice(device_status),
            "value": round(random.uniform(*value_range), 2),  # Valor dentro del rango específico
            "timestamp": datetime.datetime.utcnow().isoformat()  # Fecha y hora en ISO 8601
        }
        devices.append(device)
    
    # Guardar la lista de dispositivos en el archivo JSON
    with open(filename, "w") as f:
        json.dump(devices, f, indent=2)
    
    print(f"Se han generado {num_entries} dispositivos en el archivo '{filename}'.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Genera 10 dispositivos aleatorios en un archivo llamado "devices.json"
    generate_devices_json(num_entries=10, filename="devices.json")