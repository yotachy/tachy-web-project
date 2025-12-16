from __future__ import annotations

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ======================================================
# Home -> Introduction
# ======================================================
@app.get("/")
def home():
    return redirect(url_for("intro"))

# ======================================================
# Introduction
# base.html: url_for('intro'), active == 'intro'
# ======================================================
@app.get("/intro")
def intro():
    return render_template(
        "intro.html",
        title="Intro",
        active="intro",
    )

# ======================================================
# Macro
# base.html: url_for('macro'), active == 'macro'
# (현재는 단일 페이지로 연결. 필요 시 macro.html 내부에서 탭/카드로 확장)
# ======================================================
@app.get("/macro")
def macro():
    return render_template(
        "macro.html",
        title="Macro",
        active="macro",
    )

# ======================================================
# Crypto (category)
# base.html: url_for('crypto_category', category='spot'|'structure'|'derivatives'|'onchain')
# active: 'crypto_spot', 'crypto_structure', ...
# crypto.html uses: crypto_category variable + window.CRYPTO_CATEGORY
# ======================================================
@app.get("/crypto/<category>")
def crypto_category(category: str):
    allowed = {"spot", "structure", "derivatives", "onchain"}
    if category not in allowed:
        category = "spot"

    title_map = {
        "spot": "Crypto · Spot",
        "structure": "Crypto · Structure",
        "derivatives": "Crypto · Derivatives",
        "onchain": "Crypto · On-chain",
    }

    return render_template(
        "crypto.html",
        title=title_map.get(category, "Crypto"),
        active=f"crypto_{category}",
        crypto_category=category,
    )

# (선택) /crypto 로 들어오면 기본 spot으로
@app.get("/crypto")
def crypto_root():
    return redirect(url_for("crypto_category", category="spot"))

# ======================================================
# Local run
# ======================================================
if __name__ == "__main__":
    # Codespaces 환경 고려
    app.run(host="0.0.0.0", port=5000, debug=True)
