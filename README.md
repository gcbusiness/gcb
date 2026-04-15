# Meta Ads + Orgánico Dashboard (Streamlit)

## Qué poner en el campo de archivo en Streamlit Cloud
Según la pantalla de Streamlit Cloud, te puede pedir una de estas 2 opciones:

1. **Main file path** (solo ruta):
```text
app.py
```

2. **URL de GitHub al archivo Python**:
```text
https://github.com/<username>/<repo>/blob/<branch>/app.py
```

> No pongas rutas de archivos Markdown (`.md`) o CSV (`.csv`). Debe apuntar a un archivo `.py`.

## Error: `This file is not a valid Python script`
Si aparece ese error, normalmente es por una de estas causas:

1. En **Main file path** pusiste otro archivo distinto a `app.py`.
2. El archivo no existe en la rama seleccionada.
3. Seleccionaste otra rama distinta a donde está el archivo.
4. Escribiste una ruta incorrecta, por ejemplo:
   - `./app.py` (a veces falla según configuración)
   - `dashboard_meta_ads_kpis.md`
   - `data/sample_marketing_daily.csv`

## Configuración correcta en Streamlit Cloud
- **Repository**: tu repo
- **Branch**: la rama donde está `app.py` (ej. `main`)
- **Main file path**: `app.py` o URL GitHub al `.py`
- **Python version**: 3.11 (recomendado)

## Ejecutar local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## URL correcta para compartir
Comparte la URL final de la app con formato:

```text
https://tu-app.streamlit.app
```

No compartas `https://share.streamlit.io` porque esa es la consola de despliegue.
