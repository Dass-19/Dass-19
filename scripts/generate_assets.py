"""Generate custom animated SVGs (dark & light) for the Dass-19 GitHub Profile README.

Design synthesis:
- Pixel emblem & 4-bar palette from Dass-19/dass-aos (feat/TUI):
  Gold #b89146 | Steel Blue #537195 | Terracotta #844747 | Sage #5b635d
- Architectural monospace typography inspired by DhritiVaz
- Editorial numbered Selected Works cards inspired by lesquel
- Telemetry dashboard (language distribution, shipping velocity, KPIs) inspired by Sharann-del

Zero external dependencies. Run:
    python scripts/generate_assets.py
"""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

FONT = "'SF Mono', 'Fira Code', 'Cascadia Code', ui-monospace, Menlo, Consolas, monospace"

# DASS-AOS Signature Palette
PALETTE = {
    "gold": "#b89146",
    "gold_hi": "#dfb462",
    "blue": "#537195",
    "blue_hi": "#789ec9",
    "red": "#844747",
    "red_hi": "#b56969",
    "sage": "#5b635d",
    "sage_hi": "#87948a",
}

THEMES = {
    "dark": {
        "bg": "none",
        "card_bg": "#0d1117",
        "surface": "#131922",
        "border": "#262e3a",
        "border_soft": "#1c232d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "dim": "#606a76",
        "tag_bg": "#141a23",
        "tag_border": "#2a3340",
        "tag_text": "#a6b1be",
        "bar_track": "#1a212c",
        "emblem_bg": "#0b111a",
        "emblem_fg": "#f8fafc",
        "gold": "#d4a957",
        "blue": "#6c91bc",
        "red": "#a85f5f",
        "sage": "#7a857d",
    },
    "light": {
        "bg": "none",
        "card_bg": "#ffffff",
        "surface": "#f6f8fa",
        "border": "#d0d7de",
        "border_soft": "#e5e9ef",
        "text": "#1f2328",
        "muted": "#57606a",
        "dim": "#76808a",
        "tag_bg": "#f6f8fa",
        "tag_border": "#d0d7de",
        "tag_text": "#4b5563",
        "bar_track": "#eaeef2",
        "emblem_bg": "#0b111a",
        "emblem_fg": "#f8fafc",
        "gold": "#9e7830",
        "blue": "#3f5d80",
        "red": "#7c3b3b",
        "sage": "#4d5650",
    },
}

HIGHLIGHTS = [
    ("AWARD", "gold", "1st Place · IEEE Mobility AI Hackathon (ETCM - IHTC 2026)"),
    ("COMMUNITY", "blue", "Core Team · AWS Student Builder Group @ Universidad de Guayaquil"),
]

WORKS = [
    {
        "num": "01",
        "accent": "gold",
        "title": "DASS-AOS — Agent Operating System",
        "repo": "dass-aos",
        "tags": ["python", "tui", "zero-deps", "ai-agents"],
        "desc1": "Persistent memory, verifiable contracts, and a real-time terminal command center",
        "desc2": "for steering AI coding agents without losing architectural control of a project.",
    },
    {
        "num": "02",
        "accent": "blue",
        "title": "Godzilla — Real-Time ENSO Flood Pipeline",
        "repo": "Godzilla-EnsoStreamingPipeline",
        "tags": ["kafka", "spark", "hdfs", "fastapi"],
        "desc1": "End-to-end streaming architecture ingesting NOAA, INAMHI & NASA climate feeds",
        "desc2": "into an HDFS Parquet data lake with a live OpenStreetMap flood-risk dashboard.",
    },
    {
        "num": "03",
        "accent": "red",
        "title": "LongoApp — Speech-to-Kichwa Translator",
        "repo": "longoApp",
        "tags": ["whisper", "nllb-200", "docker", "gcp"],
        "desc1": "Multilingual multimedia ASR & neural machine translation from Spanish/English",
        "desc2": "directly into Ecuadorian Kichwa, served via FastAPI on GCP and Vercel.",
    },
    {
        "num": "04",
        "accent": "sage",
        "title": "AgentMVP — Grounded Healthcare RAG",
        "repo": "agentMvp",
        "tags": ["langgraph", "pgvector", "llama-3", "fastapi"],
        "desc1": "Multi-turn clinical assistant backend powered by LangGraph & Supabase pgvector,",
        "desc2": "delivering semantic retrieval and grounded responses with cited medical sources.",
    },
    {
        "num": "05",
        "accent": "gold",
        "title": "FraudIA — Hybrid Insurance Fraud Engine",
        "repo": "fraudIA-Novo-2S1R",
        "tags": ["shap", "gemini", "postgres", "ml"],
        "desc1": "Combines deterministic rules, ML classification, SHAP explainability and a",
        "desc2": "natural-language SQL agent for batch scoring and analytical fraud investigation.",
    },
]

# Real GitHub telemetry for Dass-19 (queried via GitHub GraphQL)
TELEMETRY = {
    "languages": [
        ("jupyter", 36, "gold"),
        ("typescript", 24, "blue"),
        ("python", 20, "red"),
        ("javascript", 16, "sage"),
        ("sql · web", 4, "blue"),
    ],
    "velocity": [
        ("'24", 1),
        ("'25", 99),
        ("'26", 360),
    ],
    "kpis": [
        ("22", "REPOSITORIES"),
        ("360", "2026 CONTRIBUTIONS"),
        ("3", "CLOUD CERTIFICATIONS"),
        ("∞", "AGENT SESSIONS OPEN"),
    ],
    "github_stats": [
        ("2026 CONTRIBUTIONS", "360"),
        ("2026 COMMITS", "168"),
        ("PUBLIC REPOSITORIES", "18"),
        ("PRIVATE BUILDS", "4"),
        ("CLOUD CREDENTIALS", "3"),
    ],
    "focus_meters": [
        ("AI / AGENTS & RAG", 92, "gold"),
        ("SOFTWARE & FULL-STACK", 88, "blue"),
        ("BIG DATA & STREAMING", 82, "red"),
        ("ML / DEEP LEARNING", 80, "sage"),
        ("CLOUD & EVENT-DRIVEN", 78, "gold"),
    ],
}

STACK_GRID = [
    {
        "idx": "01",
        "accent": "gold",
        "title": "AI · AGENTS · ML",
        "items": ["python", "pytorch", "tensorflow", "langchain", "langgraph", "hugging face", "scikit-learn", "spacy"],
    },
    {
        "idx": "02",
        "accent": "blue",
        "title": "SOFTWARE · BACKEND",
        "items": ["fastapi", "django", "flask", "typescript", "javascript", "event-driven", "docker", "git · gitlab"],
    },
    {
        "idx": "03",
        "accent": "red",
        "title": "DATA ENGINEERING",
        "items": ["apache kafka", "apache spark", "hadoop", "pyspark", "postgresql", "mongodb", "supabase", "pentaho"],
    },
    {
        "idx": "04",
        "accent": "sage",
        "title": "CLOUD · ANALYTICS",
        "items": ["azure", "aws", "gcp", "pandas", "numpy", "power bi", "tableau", "streamlit"],
    },
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def write_svg(name: str, content: str) -> None:
    path = ASSETS / name
    path.write_text(content.strip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# 1. HERO (Exact DASS pixel emblem + glow/sheen + editorial monospace header)
# ---------------------------------------------------------------------------
DASS_EMBLEM_RECTS = """
    <rect x="77" y="10" width="500" height="10"/>
    <rect x="62" y="20" width="10" height="10"/>
    <rect x="572" y="20" width="10" height="10"/>
    <rect x="57" y="30" width="10" height="10"/>
    <rect x="167" y="30" width="80" height="10"/>
    <rect x="287" y="30" width="50" height="10"/>
    <rect x="377" y="30" width="80" height="10"/>
    <rect x="477" y="30" width="80" height="10"/>
    <rect x="567" y="30" width="10" height="10"/>
    <rect x="52" y="40" width="10" height="10"/>
    <rect x="162" y="40" width="90" height="10"/>
    <rect x="272" y="40" width="70" height="10"/>
    <rect x="362" y="40" width="90" height="10"/>
    <rect x="462" y="40" width="90" height="10"/>
    <rect x="562" y="40" width="10" height="10"/>
    <rect x="47" y="50" width="10" height="10"/>
    <rect x="157" y="50" width="30" height="10"/>
    <rect x="217" y="50" width="30" height="10"/>
    <rect x="257" y="50" width="30" height="10"/>
    <rect x="317" y="50" width="30" height="10"/>
    <rect x="357" y="50" width="30" height="10"/>
    <rect x="457" y="50" width="30" height="10"/>
    <rect x="557" y="50" width="10" height="10"/>
    <rect x="42" y="60" width="10" height="10"/>
    <rect x="152" y="60" width="30" height="10"/>
    <rect x="212" y="60" width="30" height="10"/>
    <rect x="252" y="60" width="30" height="10"/>
    <rect x="312" y="60" width="30" height="10"/>
    <rect x="352" y="60" width="80" height="10"/>
    <rect x="452" y="60" width="80" height="10"/>
    <rect x="552" y="60" width="10" height="10"/>
    <rect x="37" y="70" width="10" height="10"/>
    <rect x="147" y="70" width="30" height="10"/>
    <rect x="207" y="70" width="30" height="10"/>
    <rect x="247" y="70" width="90" height="10"/>
    <rect x="357" y="70" width="80" height="10"/>
    <rect x="457" y="70" width="80" height="10"/>
    <rect x="547" y="70" width="10" height="10"/>
    <rect x="32" y="80" width="10" height="10"/>
    <rect x="142" y="80" width="30" height="10"/>
    <rect x="202" y="80" width="30" height="10"/>
    <rect x="242" y="80" width="90" height="10"/>
    <rect x="402" y="80" width="30" height="10"/>
    <rect x="502" y="80" width="30" height="10"/>
    <rect x="542" y="80" width="10" height="10"/>
    <rect x="27" y="90" width="10" height="10"/>
    <rect x="137" y="90" width="90" height="10"/>
    <rect x="237" y="90" width="30" height="10"/>
    <rect x="297" y="90" width="30" height="10"/>
    <rect x="337" y="90" width="90" height="10"/>
    <rect x="437" y="90" width="90" height="10"/>
    <rect x="537" y="90" width="10" height="10"/>
    <rect x="22" y="100" width="10" height="10"/>
    <rect x="132" y="100" width="80" height="10"/>
    <rect x="232" y="100" width="30" height="10"/>
    <rect x="292" y="100" width="30" height="10"/>
    <rect x="332" y="100" width="80" height="10"/>
    <rect x="432" y="100" width="80" height="10"/>
    <rect x="532" y="100" width="10" height="10"/>
    <rect x="17" y="110" width="10" height="10"/>
    <rect x="527" y="110" width="10" height="10"/>
    <rect x="22" y="120" width="500" height="10"/>
"""


def build_hero(mode: str) -> str:
    t = THEMES[mode]
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 300" width="880" height="300" role="img" aria-label="Daniel Suárez — DASS — Software Developer, Data Science &amp; AI Engineering" font-family="{FONT}">
  <defs>
    <style>
      .bar {{ transform-box: fill-box; transform-origin: left center; }}
      .bar-0 {{ animation: barPulse 4.4s ease-in-out infinite 0.00s; }}
      .bar-1 {{ animation: barPulse 4.4s ease-in-out infinite 0.28s; }}
      .bar-2 {{ animation: barPulse 4.4s ease-in-out infinite 0.56s; }}
      .bar-3 {{ animation: barPulse 4.4s ease-in-out infinite 0.84s; }}
      @keyframes barPulse {{
        0%, 100% {{ filter: brightness(1.0); opacity: 0.90; }}
        20%      {{ filter: brightness(1.48); opacity: 1.00; }}
        44%      {{ filter: brightness(1.0); opacity: 0.90; }}
      }}
      .sheen {{ animation: sweep 5.2s ease-in-out infinite; }}
      @keyframes sweep {{
        0%, 56%  {{ transform: translateX(-180px); opacity: 0; }}
        70%      {{ opacity: 0.28; }}
        92%      {{ transform: translateX(680px); opacity: 0; }}
        100%     {{ transform: translateX(680px); opacity: 0; }}
      }}
      .aura {{ animation: auraBreath 4.8s ease-in-out infinite; }}
      @keyframes auraBreath {{
        0%, 100% {{ opacity: 0.22; }}
        50%      {{ opacity: 0.52; }}
      }}
      .dot-ring {{ transform-box: fill-box; transform-origin: center; animation: ping 2.8s cubic-bezier(0,0,0.2,1) infinite; }}
      @keyframes ping {{
        0%   {{ transform: scale(1); opacity: 0.75; }}
        75%  {{ transform: scale(2.4); opacity: 0; }}
        100% {{ transform: scale(2.4); opacity: 0; }}
      }}
      .s0 {{ animation: segGlow 4.2s ease-in-out infinite 0.0s; }}
      .s1 {{ animation: segGlow 4.2s ease-in-out infinite 0.3s; }}
      .s2 {{ animation: segGlow 4.2s ease-in-out infinite 0.6s; }}
      .s3 {{ animation: segGlow 4.2s ease-in-out infinite 0.9s; }}
      @keyframes segGlow {{
        0%, 100% {{ opacity: 0.58; }}
        25%      {{ opacity: 1.00; }}
        55%      {{ opacity: 0.58; }}
      }}
      .cursor {{ animation: blink 1.15s step-end infinite; }}
      @keyframes blink {{
        0%, 49%  {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .bar-0, .bar-1, .bar-2, .bar-3, .sheen, .aura, .dot-ring, .s0, .s1, .s2, .s3, .cursor {{ animation: none; }}
      }}
    </style>

    <clipPath id="emblem-clip"><polygon points="77,10 577,10 517,130 17,130"/></clipPath>

    <linearGradient id="sheen-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="hero-aura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{PALETTE['gold']}" stop-opacity="0.40"/>
      <stop offset="45%" stop-color="{PALETTE['blue']}" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="{PALETTE['blue']}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Subtle ambient glow behind the DASS emblem -->
  <ellipse class="aura" cx="440" cy="86" rx="280" ry="52" fill="url(#hero-aura)"/>

  <!-- Top meta bar (DhritiVaz architectural style) -->
  <text x="20" y="20" font-size="9.5" fill="{t['muted']}" letter-spacing="2.2">DANIEL SUÁREZ · GUAYAQUIL, EC</text>
  <circle class="dot-ring" cx="702" cy="16.5" r="3.2" fill="{t['gold']}"/>
  <circle cx="702" cy="16.5" r="2.8" fill="{t['gold']}"/>
  <text x="712" y="20" font-size="9" fill="{t['muted']}" letter-spacing="1.5">SOFTWARE · DATA · AI</text>

  <!-- DASS Pixel Emblem (centered, scaled cleanly to 400x93.5) -->
  <g transform="translate(240, 38) scale(0.668)">
    <polygon points="77,10 577,10 517,130 17,130" fill="{t['emblem_bg']}"/>
    <g class="bar bar-0" fill="{PALETTE['gold']}">
      <rect x="77" y="30" width="80" height="10" rx="1"/>
      <rect x="72" y="40" width="80" height="9" rx="1"/>
    </g>
    <g class="bar bar-1" fill="{PALETTE['blue']}">
      <rect x="67" y="50" width="80" height="10" rx="1"/>
      <rect x="62" y="60" width="80" height="9" rx="1"/>
    </g>
    <g class="bar bar-2" fill="{PALETTE['red']}">
      <rect x="57" y="70" width="80" height="10" rx="1"/>
      <rect x="52" y="80" width="80" height="9" rx="1"/>
    </g>
    <g class="bar bar-3" fill="{PALETTE['sage']}">
      <rect x="47" y="90" width="80" height="10" rx="1"/>
      <rect x="42" y="100" width="80" height="9" rx="1"/>
    </g>
    <g fill="{t['emblem_fg']}">
      {DASS_EMBLEM_RECTS}
    </g>
    <g clip-path="url(#emblem-clip)">
      <polygon class="sheen" points="60,0 130,0 75,140 5,140" fill="url(#sheen-grad)"/>
    </g>
  </g>

  <!-- Editorial Monospace Tagline -->
  <text x="440" y="170" text-anchor="middle" font-size="19" font-weight="600" fill="{t['text']}" letter-spacing="0.4">
    Building <tspan fill="{t['gold']}">my dreams</tspan>, building <tspan fill="{t['blue']}">a history.</tspan><tspan class="cursor" fill="{t['gold']}">_</tspan>
  </text>

  <text x="440" y="198" text-anchor="middle" font-size="11.2" fill="{t['muted']}" letter-spacing="0.45">
    software development · data science &amp; ai engineering @ universidad de guayaquil
  </text>
  <text x="440" y="218" text-anchor="middle" font-size="10.2" fill="{t['dim']}" letter-spacing="0.55">
    full-stack &amp; event-driven systems · rag &amp; multi-agent workflows · real-time data pipelines
  </text>

  <!-- Animated 4-segment slanted DASS accent bar -->
  <g transform="translate(180, 244) scale(0.591, 1)">
    <polygon class="s0" points="4,0 218,0 213,5 0,5" fill="{PALETTE['gold']}"/>
    <polygon class="s1" points="223,0 438,0 433,5 218,5" fill="{PALETTE['blue']}"/>
    <polygon class="s2" points="443,0 658,0 653,5 438,5" fill="{PALETTE['red']}"/>
    <polygon class="s3" points="663,0 880,0 875,5 658,5" fill="{PALETTE['sage']}"/>
  </g>

  <!-- Subtle bottom micro-caption -->
  <text x="440" y="276" text-anchor="middle" font-size="9.2" fill="{t['dim']}" letter-spacing="1.8">
    I LOVE MY FAMILY AND MUSIC  ·  AZURE · GCP · AWS
  </text>
</svg>
"""


# ---------------------------------------------------------------------------
# 2. SECTION HEADERS (Sharann-del numbered architectural divider)
# ---------------------------------------------------------------------------
def build_section_header(num: str, label: str, path_hint: str, accent_key: str, mode: str) -> str:
    t = THEMES[mode]
    accent = t[accent_key]
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 42" width="880" height="42" role="img" aria-label="{num} {esc(label)}" font-family="{FONT}">
  <defs>
    <style>
      .pulse {{ animation: numGlow 4s ease-in-out infinite; }}
      @keyframes numGlow {{
        0%, 100% {{ opacity: 0.80; }}
        50%      {{ opacity: 1.00; }}
      }}
      @media (prefers-reduced-motion: reduce) {{ .pulse {{ animation: none; }} }}
    </style>
  </defs>
  <text class="pulse" x="20" y="29" font-size="22" font-weight="600" fill="{accent}" letter-spacing="1">{num}</text>
  <text x="64" y="26" font-size="11" font-weight="600" fill="{t['text']}" letter-spacing="3.2">{esc(label)}</text>
  <line x1="275" y1="22" x2="725" y2="22" stroke="{t['border']}" stroke-width="0.75"/>
  <text x="860" y="26" text-anchor="end" font-size="10" fill="{t['dim']}" letter-spacing="0.8">{esc(path_hint)}</text>
</svg>
"""


# ---------------------------------------------------------------------------
# 2B. SUBTLE HIGHLIGHTS STRIP (Understated details: Role, IEEE Award, AWS SBG)
# ---------------------------------------------------------------------------
def build_highlights(mode: str) -> str:
    t = THEMES[mode]
    rows = []
    for i, (tag, acc, text) in enumerate(HIGHLIGHTS):
        y = 26 + i * 26
        color = t[acc]
        rows.append(
            f'<rect x="36" y="{y - 11}" width="84" height="16" rx="2" fill="{t["tag_bg"]}" stroke="{t["tag_border"]}" stroke-width="0.6"/>'
            f'<text x="78" y="{y}" text-anchor="middle" font-size="8.5" font-weight="600" fill="{color}" letter-spacing="1.2">{esc(tag)}</text>'
            f'<text x="134" y="{y}" font-size="10.2" fill="{t["muted"]}" letter-spacing="0.2">{esc(text)}</text>'
        )
    rows_svg = "\n  ".join(rows)
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 70" width="880" height="70" role="img" aria-label="Award and Community Highlights" font-family="{FONT}">
  <rect x="20" y="6" width="840" height="58" rx="2" fill="none" stroke="{t['border_soft']}" stroke-width="0.75"/>
  {rows_svg}
</svg>
"""


# ---------------------------------------------------------------------------
# 3. SELECTED WORK CARDS (Clickable modular SVGs — lesquel + DhritiVaz)
# ---------------------------------------------------------------------------
def build_work_card(work: dict, mode: str, idx: int) -> str:
    t = THEMES[mode]
    accent = t[work["accent"]]
    delay = f"{idx * 0.45:.2f}s"

    pills_svg = []
    cursor_x = 856
    for tag in reversed(work["tags"]):
        w = max(46, len(tag) * 6.5 + 16)
        cursor_x -= w
        pills_svg.append(
            f'<rect x="{cursor_x:.1f}" y="19" width="{w:.1f}" height="18" rx="2" '
            f'fill="{t["tag_bg"]}" stroke="{t["tag_border"]}" stroke-width="0.6"/>'
            f'<text x="{cursor_x + w/2:.1f}" y="31" text-anchor="middle" font-size="9" '
            f'fill="{t["tag_text"]}" letter-spacing="0.3">{esc(tag)}</text>'
        )
        cursor_x -= 6
    pills_markup = "\n  ".join(pills_svg)

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 106" width="880" height="106" role="img" aria-label="{esc(work['title'])}" font-family="{FONT}">
  <defs>
    <style>
      .bar-glow {{ animation: cardPulse 4.6s ease-in-out infinite {delay}; }}
      @keyframes cardPulse {{
        0%, 100% {{ opacity: 0.55; }}
        30%      {{ opacity: 1.00; }}
        60%      {{ opacity: 0.55; }}
      }}
      @media (prefers-reduced-motion: reduce) {{ .bar-glow {{ animation: none; }} }}
    </style>
  </defs>

  <rect class="bar-glow" x="20" y="18" width="3" height="68" rx="1.5" fill="{accent}"/>
  <text x="38" y="33" font-size="11" font-weight="600" fill="{accent}" letter-spacing="1.2">{work['num']}</text>
  <text x="70" y="33" font-size="14" font-weight="600" fill="{t['text']}" letter-spacing="0.2">{esc(work['title'])}</text>
  {pills_markup}
  <text x="70" y="56" font-size="10.8" fill="{t['muted']}" letter-spacing="0.15">{esc(work['desc1'])}</text>
  <text x="70" y="73" font-size="10.8" fill="{t['muted']}" letter-spacing="0.15">{esc(work['desc2'])}</text>
  <text x="856" y="88" text-anchor="end" font-size="9.2" fill="{t['dim']}" letter-spacing="0.5">{esc(work['repo'])} ↗</text>
  <line x1="20" y1="104" x2="860" y2="104" stroke="{t['border_soft']}" stroke-width="0.75"/>
</svg>
"""


# ---------------------------------------------------------------------------
# 4. TELEMETRY DASHBOARD (Sharann-del inspired + DASS palette + glow)
# ---------------------------------------------------------------------------
def build_telemetry(mode: str) -> str:
    t = THEMES[mode]

    lang_rows = []
    y0 = 86
    for i, (lang, pct, acc) in enumerate(TELEMETRY["languages"]):
        y = y0 + i * 32
        bar_max = 215
        bar_w = max(10, bar_max * (pct / 40.0))
        color = t[acc]
        delay = f"{i * 0.35:.2f}s"
        lang_rows.append(
            f'<text x="20" y="{y}" font-size="10" fill="{t["text"]}" letter-spacing="0.5">{esc(lang)}</text>'
            f'<rect x="20" y="{y + 7}" width="{bar_max}" height="5" rx="1" fill="{t["bar_track"]}"/>'
            f'<rect class="tbar" style="animation-delay:{delay}" x="20" y="{y + 7}" width="{bar_w:.1f}" height="5" rx="1" fill="{color}"/>'
            f'<text x="{20 + bar_max + 10}" y="{y + 12}" font-size="9.5" fill="{t["muted"]}">{pct}%</text>'
        )
    langs_svg = "\n  ".join(lang_rows)

    vel_path = "M 338,206 C 382,204 415,188 447,178 C 482,167 518,125 556,98"
    vel_area = vel_path + " L 556,210 L 338,210 Z"

    kpi_rows = []
    for i, (val, label) in enumerate(TELEMETRY["kpis"]):
        y = 104 + i * 39
        val_color = t["gold"] if i == 1 else t["text"]
        kpi_rows.append(
            f'<text x="612" y="{y}" font-size="23" font-weight="600" fill="{val_color}" letter-spacing="0.5">{esc(val)}</text>'
            f'<text x="676" y="{y - 4}" font-size="9" fill="{t["muted"]}" letter-spacing="1.5">{esc(label)}</text>'
        )
    kpis_svg = "\n  ".join(kpi_rows)

    gh_rows = []
    for i, (k, v) in enumerate(TELEMETRY["github_stats"]):
        y = 326 + i * 22
        gh_rows.append(
            f'<text x="40" y="{y}" font-size="9.5" fill="{t["muted"]}" letter-spacing="1.2">{esc(k)}</text>'
            f'<text x="408" y="{y}" text-anchor="end" font-size="10.5" font-weight="600" fill="{t["text"]}">{esc(v)}</text>'
        )
    gh_svg = "\n  ".join(gh_rows)

    focus_rows = []
    for i, (k, pct, acc) in enumerate(TELEMETRY["focus_meters"]):
        y = 326 + i * 22
        color = t[acc]
        track_x = 636
        track_w = 200
        fill_w = track_w * (pct / 100.0)
        delay = f"{i * 0.4:.2f}s"
        focus_rows.append(
            f'<text x="472" y="{y}" font-size="9.2" fill="{t["muted"]}" letter-spacing="0.8">{esc(k)}</text>'
            f'<rect x="{track_x}" y="{y - 8}" width="{track_w}" height="8" rx="1" fill="{t["bar_track"]}" stroke="{t["border"]}" stroke-width="0.6"/>'
            f'<rect class="tbar" style="animation-delay:{delay}" x="{track_x}" y="{y - 8}" width="{fill_w:.1f}" height="8" rx="1" fill="{color}"/>'
        )
    focus_svg = "\n  ".join(focus_rows)

    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 456" width="880" height="456" role="img" aria-label="Telemetry Dashboard — Language Distribution, Shipping Velocity, and GitHub Metrics" font-family="{FONT}">
  <defs>
    <style>
      .tbar {{ animation: barGlow 4.5s ease-in-out infinite; }}
      @keyframes barGlow {{
        0%, 100% {{ opacity: 0.82; }}
        35%      {{ opacity: 1.00; }}
        70%      {{ opacity: 0.82; }}
      }}
      .node-halo {{ transform-box: fill-box; transform-origin: center; animation: haloPing 2.8s ease-out infinite; }}
      @keyframes haloPing {{
        0%   {{ transform: scale(1); opacity: 0.85; }}
        80%  {{ transform: scale(2.8); opacity: 0; }}
        100% {{ transform: scale(2.8); opacity: 0; }}
      }}
      .vel-line {{ animation: shimmerLine 5s ease-in-out infinite; }}
      @keyframes shimmerLine {{
        0%, 100% {{ opacity: 0.88; }}
        50%      {{ opacity: 1.00; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .tbar, .node-halo, .vel-line {{ animation: none; }}
      }}
    </style>

    <linearGradient id="vel-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{t['gold']}" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="{t['gold']}" stop-opacity="0.00"/>
    </linearGradient>

    <linearGradient id="vel-stroke" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['blue']}"/>
      <stop offset="60%" stop-color="{t['gold']}"/>
      <stop offset="100%" stop-color="{PALETTE['gold_hi']}"/>
    </linearGradient>
  </defs>

  <text x="20" y="20" font-size="9.5" fill="{t['text']}" letter-spacing="2">TELEMETRY — WHAT THE HANDS ARE DOING</text>
  <text x="860" y="20" text-anchor="end" font-size="9.5" fill="{t['dim']}" letter-spacing="1.6">FIG. 02</text>
  <line x1="20" y1="31" x2="860" y2="31" stroke="{t['border']}" stroke-width="0.75"/>

  <text x="20" y="58" font-size="9" fill="{t['muted']}" letter-spacing="1.6">LANGUAGE DISTRIBUTION · EST.</text>
  <text x="334" y="58" font-size="9" fill="{t['muted']}" letter-spacing="1.6">SHIPPING VELOCITY · 2024 → 2026</text>

  <line x1="306" y1="50" x2="306" y2="238" stroke="{t['border_soft']}" stroke-width="0.75"/>
  <line x1="586" y1="50" x2="586" y2="238" stroke="{t['border_soft']}" stroke-width="0.75"/>

  {langs_svg}

  <line x1="334" y1="210" x2="564" y2="210" stroke="{t['border']}" stroke-width="0.75"/>
  <path d="{vel_area}" fill="url(#vel-grad)"/>
  <path class="vel-line" d="{vel_path}" fill="none" stroke="url(#vel-stroke)" stroke-width="2" stroke-linecap="round"/>

  <circle cx="338" cy="206" r="2.5" fill="{t['blue']}"/>
  <circle cx="447" cy="178" r="2.8" fill="{t['gold']}"/>
  <circle class="node-halo" cx="556" cy="98" r="4.5" fill="{t['gold']}"/>
  <circle cx="556" cy="98" r="3.5" fill="{PALETTE['gold_hi']}" stroke="{t['card_bg']}" stroke-width="1"/>
  <text x="556" y="85" text-anchor="end" font-size="9" font-weight="600" fill="{t['gold']}">360</text>

  <text x="338" y="226" font-size="8.5" fill="{t['dim']}">'24</text>
  <text x="447" y="226" text-anchor="middle" font-size="8.5" fill="{t['dim']}">'25</text>
  <text x="556" y="226" text-anchor="end" font-size="8.5" fill="{t['dim']}">'26</text>
  <text x="334" y="248" font-size="9.5" fill="{t['muted']}" letter-spacing="0.6">trend — <tspan fill="{t['gold']}">accelerating</tspan></text>

  {kpis_svg}

  <rect x="20" y="274" width="408" height="164" rx="2" fill="none" stroke="{t['border']}" stroke-width="0.75"/>
  <text x="40" y="298" font-size="9.5" font-weight="600" fill="{t['text']}" letter-spacing="2">GITHUB TELEMETRY</text>
  <line x1="40" y1="308" x2="408" y2="308" stroke="{t['border_soft']}" stroke-width="0.75"/>
  {gh_svg}

  <rect x="452" y="274" width="408" height="164" rx="2" fill="none" stroke="{t['border']}" stroke-width="0.75"/>
  <text x="472" y="298" font-size="9.5" font-weight="600" fill="{t['text']}" letter-spacing="2">CORE FOCUS AREAS</text>
  <line x1="472" y1="308" x2="840" y2="308" stroke="{t['border_soft']}" stroke-width="0.75"/>
  {focus_svg}
</svg>
"""


# ---------------------------------------------------------------------------
# 5. ARCHITECTURAL 2x2 STACK MATRIX (DhritiVaz inspired + DASS accents)
# ---------------------------------------------------------------------------
def build_stack(mode: str) -> str:
    t = THEMES[mode]
    cells = []
    coords = [(20, 12), (440, 12), (20, 140), (440, 140)]

    for (cx, cy), group in zip(coords, STACK_GRID):
        accent = t[group["accent"]]
        cells.append(
            f'<text x="{cx + 20}" y="{cy + 30}" font-size="9.5" font-weight="600" fill="{accent}" letter-spacing="1.4">{group["idx"]}</text>'
            f'<text x="{cx + 42}" y="{cy + 30}" font-size="10.5" font-weight="600" fill="{t["text"]}" letter-spacing="1.8">{esc(group["title"])}</text>'
        )
        px = cx + 20
        py = cy + 48
        max_x = cx + 400
        for item in group["items"]:
            w = max(56, len(item) * 6.4 + 18)
            if px + w > max_x:
                px = cx + 20
                py += 28
            cells.append(
                f'<rect x="{px:.1f}" y="{py}" width="{w:.1f}" height="21" rx="2" '
                f'fill="{t["tag_bg"]}" stroke="{t["tag_border"]}" stroke-width="0.6"/>'
                f'<text x="{px + w/2:.1f}" y="{py + 13.5}" text-anchor="middle" font-size="9.5" '
                f'fill="{t["tag_text"]}" letter-spacing="0.2">{esc(item)}</text>'
            )
            px += w + 7

    cells_svg = "\n  ".join(cells)
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 280" width="880" height="280" role="img" aria-label="Tech Stack and Capabilities Matrix" font-family="{FONT}">
  <rect x="20" y="12" width="840" height="256" rx="2" fill="none" stroke="{t['border']}" stroke-width="0.75"/>
  <line x1="440" y1="12" x2="440" y2="268" stroke="{t['border']}" stroke-width="0.75"/>
  <line x1="20" y1="140" x2="860" y2="140" stroke="{t['border']}" stroke-width="0.75"/>
  {cells_svg}
</svg>
"""


# ---------------------------------------------------------------------------
# 6. FOOTER (Animated 4-bar slanted accent + minimalist sign-off)
# ---------------------------------------------------------------------------
def build_footer(mode: str) -> str:
    t = THEMES[mode]
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 68" width="880" height="68" role="img" aria-label="Don't be afraid. — Dass-19" font-family="{FONT}">
  <defs>
    <style>
      .s0 {{ animation: fGlow 4.2s ease-in-out infinite 0.0s; }}
      .s1 {{ animation: fGlow 4.2s ease-in-out infinite 0.3s; }}
      .s2 {{ animation: fGlow 4.2s ease-in-out infinite 0.6s; }}
      .s3 {{ animation: fGlow 4.2s ease-in-out infinite 0.9s; }}
      @keyframes fGlow {{
        0%, 100% {{ opacity: 0.52; }}
        25%      {{ opacity: 1.00; }}
        55%      {{ opacity: 0.52; }}
      }}
      @media (prefers-reduced-motion: reduce) {{ .s0,.s1,.s2,.s3 {{ animation: none; }} }}
    </style>
  </defs>
  <g transform="translate(20, 10) scale(0.9545, 0.7)">
    <polygon class="s0" points="4,0 218,0 213,6 0,6" fill="{PALETTE['gold']}"/>
    <polygon class="s1" points="223,0 438,0 433,6 218,6" fill="{PALETTE['blue']}"/>
    <polygon class="s2" points="443,0 658,0 653,6 438,6" fill="{PALETTE['red']}"/>
    <polygon class="s3" points="663,0 880,0 875,6 658,6" fill="{PALETTE['sage']}"/>
  </g>
  <text x="20" y="46" font-size="11" fill="{t['text']}" letter-spacing="0.8">"don't be afraid."</text>
  <text x="860" y="46" text-anchor="end" font-size="9.5" fill="{t['dim']}" letter-spacing="1.4">DASS-19 · GUAYAQUIL, ECUADOR</text>
</svg>
"""


def main() -> None:
    sections = [
        ("01", "CREDENTIALS & NOTES", "~/01-credentials", "gold"),
        ("02", "SELECTED WORKS", "~/02-selected-works", "blue"),
        ("03", "TELEMETRY", "~/03-telemetry", "red"),
        ("04", "STACK & CAPABILITIES", "~/04-stack", "sage"),
    ]

    for mode in ("dark", "light"):
        write_svg(f"hero-{mode}.svg", build_hero(mode))
        write_svg(f"highlights-{mode}.svg", build_highlights(mode))
        for num, label, hint, acc in sections:
            write_svg(f"sec-{num}-{mode}.svg", build_section_header(num, label, hint, acc, mode))
        for i, w in enumerate(WORKS):
            write_svg(f"work-{w['num']}-{mode}.svg", build_work_card(w, mode, i))
        write_svg(f"telemetry-{mode}.svg", build_telemetry(mode))
        write_svg(f"stack-{mode}.svg", build_stack(mode))
        write_svg(f"footer-{mode}.svg", build_footer(mode))

    count = len(list(ASSETS.glob("*.svg")))
    print(f"Generated {count} SVG assets in {ASSETS}")


if __name__ == "__main__":
    main()
