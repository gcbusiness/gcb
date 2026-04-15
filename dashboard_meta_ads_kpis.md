# Dashboard de Meta Ads + Crecimiento Orgánico (Plantilla)

## 1) Objetivo del dashboard
Construir un dashboard ejecutivo y operativo que permita responder, en menos de 5 minutos:
- ¿Qué tanto del crecimiento viene de pago vs. orgánico?
- ¿El tráfico pagado y orgánico está convirtiendo con rentabilidad?
- ¿Qué campañas/ad sets/creativos aportan ventas incrementales y cuáles drenan presupuesto?

---

## 2) KPIs clave (priorizados)

### A. KPIs de negocio (nivel CEO/Founder)
1. **Ingresos totales**
   - Fórmula: `Revenue Total = Revenue Paid + Revenue Organic`
2. **CAC blended (total)**
   - Fórmula: `CAC Blended = Inversión Paid / # Nuevos Clientes Totales`
3. **MER (Marketing Efficiency Ratio)**
   - Fórmula: `MER = Ingresos Totales / Inversión Paid`
4. **ROAS de Meta (plataforma)**
   - Fórmula: `ROAS Meta = Ingresos atribuidos Meta / Inversión Meta`
5. **Margen de contribución por canal**
   - Fórmula: `Margen = Ingresos - COGS - Inversión Paid - Costos variables`

### B. KPIs de adquisición (nivel performance)
6. **CTR (link)**
   - Fórmula: `CTR = Link Clicks / Impresiones`
7. **CPC (link)**
   - Fórmula: `CPC = Inversión / Link Clicks`
8. **CPM**
   - Fórmula: `CPM = (Inversión / Impresiones) * 1000`
9. **CVR sitio (Paid y Orgánico)**
   - Fórmula: `CVR = Compras / Sesiones`
10. **CPA / CPP (Costo por compra)**
    - Fórmula: `CPP = Inversión / # Compras`

### C. KPIs de embudo (funnel)
11. **View Content rate**
12. **Add to Cart rate**
13. **Initiate Checkout rate**
14. **Purchase rate**
15. **Drop-off por etapa**

> Recomendación: mostrar funnel para Paid y Orgánico en paralelo para visualizar diferencias de calidad de tráfico.

### D. KPIs de retención y calidad de cliente
16. **AOV (Ticket promedio)**
17. **LTV 30/60/90 días**
18. **nCAC Payback (días)**
19. **% nuevos vs. recurrentes**
20. **Tasa de recompra**

---

## 3) Estructura recomendada del dashboard

### Página 1 — Resumen Ejecutivo
- Tarjetas KPI: Revenue Total, Revenue Paid, Revenue Organic, CAC Blended, MER, ROAS Meta.
- Gráfica de tendencia diaria/semanal (últimos 90 días).
- Pie o barra apilada: contribución de ingresos por canal (Paid vs Orgánico).
- Meta vs Real (objetivos mensuales).

### Página 2 — Paid Media (Meta Ads)
- Tabla por campaña/ad set/ad:
  - Spend, Impressions, CPM, CTR, CPC, CVR, CPP, Purchases, Revenue, ROAS.
- Heatmap de creativos:
  - Hook, formato, ángulo, CTR, CPP, ROAS.
- Frecuencia y fatiga creativa (por semana).

### Página 3 — Orgánico
- Sesiones orgánicas por fuente (IG orgánico, TikTok orgánico, SEO, Directo, Referidos).
- Engagement vs conversión:
  - sesiones, tiempo en sitio, CVR, revenue.
- Top landing pages orgánicas y su tasa de compra.

### Página 4 — Funnel y atribución
- Funnel Paid vs Orgánico (VC → ATC → IC → Purchase).
- Modelo de atribución comparado:
  - Meta 7d click/1d view vs GA4 data-driven o last-click.
- Ventana temporal seleccionable (7/14/30/90 días).

### Página 5 — Cohortes y rentabilidad
- Cohortes por fecha de primera compra.
- LTV por cohorte (30/60/90 días).
- Payback por cohorte y por canal de adquisición.

---

## 4) Segmentaciones/Filtros indispensables
- Rango de fechas.
- País / Región.
- Dispositivo (mobile/desktop).
- Prospecting vs Retargeting.
- Campaña, ad set, creativo.
- Audiencia (broad, lookalike, intereses, CRM).
- Nuevo vs Recurrente.

---

## 5) Reglas de lectura (insights accionables)

### Señales de alerta
- **CTR baja + CPM sube** → posible fatiga creativa o audiencia saturada.
- **Buen CTR pero baja CVR** → problema de landing page, pricing o fricción checkout.
- **ROAS Meta estable pero MER cae** → menos tracción orgánica o menor efecto halo.
- **CAC Blended sube con spend estable** → caída de tasa de conversión o ticket promedio.

### Acciones sugeridas
- Rotación creativa cada 10–14 días si frecuencia alta.
- Test A/B de hooks (UGC, prueba social, oferta, dolor-beneficio).
- Mejoras de CRO en landing (velocidad, trust badges, checkout express).
- Reasignar presupuesto por contribución marginal, no solo por ROAS plataforma.

---

## 6) Definiciones de fuentes de datos
- **Meta Ads Manager**: spend, impresiones, clics, compras atribuidas, revenue atribuido.
- **GA4 / Shopify / CRM**: sesiones, compras reales, revenue neto, nuevos clientes.
- **UTMs**: obligatorias para separar orgánico/pago y validar atribución cruzada.

### Convención mínima UTM
- `utm_source`: facebook | instagram | tiktok | google | email
- `utm_medium`: paid_social | organic_social | cpc | referral
- `utm_campaign`: nombre_estandarizado
- `utm_content`: hook_formato_audiencia

---

## 7) Cadencia operativa recomendada
- **Daily (15 min):** spend, CPP, ROAS, alertas de caída.
- **Semanal (60 min):** creativos ganadores/perdedores, cambios en funnel.
- **Mensual (90 min):** MER, CAC blended, payback, LTV por cohorte.

---

## 8) Plantilla de objetivos (ejemplo)
- MER objetivo: `> 3.0`
- CAC blended objetivo: `< $45`
- ROAS Meta objetivo: `> 2.2`
- CVR sitio objetivo: `> 2.5%`
- Payback objetivo: `< 45 días`

> Ajustar objetivos según margen bruto, ciclo de compra y estacionalidad.

---

## 9) Checklist de implementación (rápido)
- [ ] Validar eventos de pixel + CAPI (Purchase, ATC, IC).
- [ ] Verificar deduplicación Pixel/CAPI.
- [ ] Estandarizar naming de campañas y UTMs.
- [ ] Conectar Meta + GA4 + ecommerce/CRM al BI (Looker Studio, Power BI o Tableau).
- [ ] Definir una “source of truth” para revenue y clientes nuevos.
- [ ] Crear alertas automáticas (Slack/Email) por umbrales.

---

## 10) SQL base (opcional, ejemplo conceptual)
```sql
SELECT
  date,
  channel_group,
  SUM(spend) AS spend,
  SUM(sessions) AS sessions,
  SUM(purchases) AS purchases,
  SUM(revenue) AS revenue,
  SAFE_DIVIDE(SUM(purchases), SUM(sessions)) AS cvr,
  SAFE_DIVIDE(SUM(spend), SUM(purchases)) AS cpp,
  SAFE_DIVIDE(SUM(revenue), SUM(spend)) AS roas
FROM marketing_daily
WHERE date BETWEEN @start_date AND @end_date
GROUP BY 1,2
ORDER BY 1,2;
```

---

## 11) Recomendación final
Para clientes que combinan crecimiento orgánico + paid, prioriza siempre métricas **blended** (MER, CAC blended, payback total) para decisiones de presupuesto, y usa ROAS de plataforma como señal táctica, no como única verdad.
