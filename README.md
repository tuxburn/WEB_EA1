# tecnologias web - Preparación AE1
# Pasos para la Ejecución del Proyecto

## 1. Descargar el Repositorio 

https://github.com/tuxburn/WEB_EA1.git

## 2. Crear un Entorno Virtual
Ejecuta el siguiente comando para crear un entorno virtual en Python:

```bash
python -m venv venv
```

## 3. Activar el Entorno Virtual
Para activar el entorno virtual, usa el siguiente comando:

```bash
source venv/Scripts/activate
```

## 4. Instalar las Dependencias
Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements
```

## 5. Ejecutar el Script `gen_data.py`
Para generar los datos de los dispositivos, ejecuta:

```bash
python src/gen_data.py
```

## 6. Ejecutar la Aplicación
Para iniciar la aplicación, ejecuta:

```bash
python src/api.py
```

---

# **Pruebas de Endpoints**

## 7.1 Obtener la Lista de Dispositivos
**Endpoint:**  
`GET http://localhost:5000/devices`

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "name": "Device 1",
    "type": "pressure",
    "status": "inactive",
    "value": 36.77,
    "timestamp": "2025-03-19T02:28:01.517392"
  },
  {
    "id": 2,
    "name": "Device 2",
    "type": "temperature",
    "status": "inactive",
    "value": 79.2,
    "timestamp": "2025-03-19T02:28:01.517415"
  }
]
```

---

## 7.2 Obtener un Dispositivo por ID
**Endpoint:**  
`GET http://localhost:5000/devices/1`

**Respuesta esperada:**
```json
{
    "id": 1,
    "name": "Device 1",
    "type": "pressure",
    "status": "inactive",
    "value": 36.77,
    "timestamp": "2025-03-19T02:28:01.517392"
  }
```

---

## 7.3 Crear un Nuevo Dispositivo
**Endpoint:**  
`POST http://localhost:5000/devices`

**Body:**
```json
{
    "name": "Device A",
    "type": "pressure",
    "status": "active",
    "value": 136.77
  }
```

**Respuesta esperada:**
```json
{
    "id": 12,
    "name": "Device A",
    "type": "pressure",
    "status": "active",
    "value": 136.77,
    "timestamp": "2025-03-19T02:28:01.517443"
  }
```

---

## 7.4 Actualizar un Dispositivo
**Endpoint:**  
`PUT http://localhost:5000/devices/1`

**Body:**
```json
{
    "name": "Device modifica",
    "type": "speed",
    "status": "active",
    "value": 90
  }
```

**Respuesta esperada:**
```json
{
    "id": 1,
    "name": "Device modifica",
    "type": "speed",
    "status": "active",
    "value": 90,
    "timestamp": "2025-03-19T02:30:44.375522"
  }
```

---

## 7.5 Eliminar un Dispositivo
**Endpoint:**  
`DELETE http://localhost:5000/devices/1`

**Respuesta esperada:**
```json
{
  "message": "Device deleted successfully"
}
```
