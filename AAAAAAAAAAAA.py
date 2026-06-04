from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────
# BASE DE DATOS DE ESTRATEGIAS
# Para añadir más, copia el bloque de una estrategia y pégalo
# debajo del último, siguiendo exactamente el mismo formato.
# Campos:
#   nombre    → Título de la estrategia
#   categoria → Etiqueta de categoría (ej. "Ahorro", "Inversión"...)
#   descripcion → Explicación breve de en qué consiste
#   pros      → Lista de ventajas (añade o quita strings libremente)
#   contras   → Lista de desventajas
# ─────────────────────────────────────────────────────────────
ESTRATEGIAS = [
    {
        "nombre": "Fondo de Emergencia",
        "categoria": "Ahorro",
        "descripcion": (
            "Consiste en reservar entre 3 y 6 meses de tus gastos fijos "
            "en una cuenta de fácil acceso. Es el primer paso de cualquier "
            "plan financiero sólido: te protege ante imprevistos sin tener "
            "que endeudarte."
        ),
        "pros": [
            "Reduce el estrés financiero ante emergencias",
            "Evita recurrir a créditos o préstamos costosos",
            "Fácil de implementar desde cualquier nivel de ingresos",
        ],
        "contras": [
            "El dinero en cuenta corriente pierde valor por la inflación",
            "Requiere disciplina para no tocarlo",
        ],
    },

    # ── AÑADE AQUÍ MÁS ESTRATEGIAS ──────────────────────────
    # {
    #     "nombre": "Regla del 50/30/20",
    #     "categoria": "Presupuesto",
    #     "descripcion": "Destina el 50% de tus ingresos a necesidades, ...",
    #     "pros": ["Fácil de recordar", "Flexible"],
    #     "contras": ["Puede no adaptarse a ingresos muy bajos"],
    # },
    # ────────────────────────────────────────────────────────
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/buscar")
def buscar():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify(ESTRATEGIAS)

    resultados = [
        e for e in ESTRATEGIAS
        if query in e["nombre"].lower()
        or query in e["categoria"].lower()
        or query in e["descripcion"].lower()
        or any(query in p.lower() for p in e["pros"])
        or any(query in c.lower() for c in e["contras"])
    ]
    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True)         