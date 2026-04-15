# Prompt de tarea para Manus AI

Copia y pega este prompt en Manus AI para que te construya el dashboard completo.

---

## PROMPT

Quiero que construyas un **dashboard profesional de marketing** para mi cliente, enfocado en **Meta Ads + crecimiento orgánico** (visión blended).

### Objetivo
Crear un dashboard ejecutivo y operativo que permita:
1) medir performance de pago vs orgánico,
2) medir performance total blended,
3) detectar oportunidades y alertas accionables,
4) compartir una URL pública estable para cliente.

### Stack requerido
- Frontend: **Streamlit**
- Datos: CSV inicialmente (luego preparado para BigQuery/Sheets/GA4)
- Visualizaciones: Plotly
- Lenguaje: Python
- Entrega: código listo para ejecutar y desplegar

### Archivos que debes generar
1. `app.py`
2. `requirements.txt`
3. `README.md`
4. `data/sample_marketing_daily.csv` (datos demo realistas)
5. `src/kpi.py` (funciones de métricas)
6. `src/validators.py` (validación de esquema)
7. `src/transform.py` (limpieza y agregaciones)
8. `.streamlit/config.toml`
9. `tests/test_kpis.py`
10. `tests/test_validators.py`

### Esquema de datos mínimo esperado
Columnas obligatorias:
- `date` (YYYY-MM-DD)
- `channel_group` (ej: `paid_meta`, `organic_social`, `organic_search`, `email`)
- `campaign`
- `adset`
- `ad_name`
- `country`
- `device`
- `spend`
- `impressions`
- `clicks`
- `sessions`
- `view_content`
- `add_to_cart`
- `initiate_checkout`
- `purchases`
- `revenue`
- `new_customers`
- `returning_customers`

### KPIs obligatorios
**Negocio (blended):**
- Revenue Total
- Revenue Paid
- Revenue Organic
- CAC Blended = Spend Paid / New Customers Total
- MER = Revenue Total / Spend Paid
- AOV = Revenue / Purchases
- CVR sitio = Purchases / Sessions
- Payback aproximado (si no hay margen, dejar fórmula parametrizable)

**Paid (Meta):**
- CPM = spend/impressions*1000
- CTR = clicks/impressions
- CPC = spend/clicks
- CPP (CPA compra) = spend/purchases
- ROAS Paid = revenue_paid/spend_paid
- Frecuencia (si no existe campo, dejar opcional)

**Funnel:**
- VC rate = view_content/sessions
- ATC rate = add_to_cart/view_content
- IC rate = initiate_checkout/add_to_cart
- Purchase rate = purchases/initiate_checkout
- Drop-off por etapa

### Funcionalidad UI (obligatoria)
- Filtros laterales:
  - rango de fechas
  - canal
  - país
  - dispositivo
  - campaign/adset/ad
  - nuevo vs recurrente
- Bloque de métricas principales (cards)
- Gráfica de tendencia diaria/semanal (revenue/spend/purchases)
- Comparativo Paid vs Orgánico
- Tabla por canal/campaña con orden y búsqueda
- Sección Funnel comparativo
- Sección Cohortes (30/60/90 días) si hay datos suficientes
- Export de tabla a CSV

### Reglas de calidad
- Separar lógica de negocio en módulos (`src/`), no meter todo en `app.py`.
- Validar columnas obligatorias y tipos con mensajes claros.
- Manejar divisiones por cero sin romper la app.
- Añadir docstrings y typing.
- Código limpio y mantenible.

### Testing
- Crear tests unitarios para:
  - fórmulas KPI
  - validación de columnas
  - edge cases (cero spend, cero sessions, NaN)
- Comando de test: `pytest -q`

### Deploy
- Incluir guía para deploy en Streamlit Community Cloud.
- Importante: explicar que la URL para compartir es `https://<app>.streamlit.app` (no `share.streamlit.io`).
- Incluir sección troubleshooting para `HTTP ERROR 401`:
  - app privada
  - repo privado
  - sesión expirada
  - restricciones por red corporativa

### Entregables finales
Quiero que me entregues:
1. Estructura final de archivos,
2. código completo,
3. instrucciones para correr local,
4. instrucciones de deploy,
5. checklist de validación funcional.

Genera todo el proyecto listo para copiar/pegar y ejecutar.

---

## Prompt corto (alternativo)

Crea una app Streamlit production-ready para dashboard de Meta Ads + orgánico con KPIs blended (MER, CAC blended, ROAS, CVR, AOV), filtros avanzados, funnel, tabla por campaña, validación robusta de datos, tests con pytest y deploy guide en Streamlit Cloud, incluyendo troubleshooting de HTTP 401. Entrégame estructura de archivos + código completo + sample data + pasos de ejecución/deploy.
