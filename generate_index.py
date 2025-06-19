from datetime import datetime

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Recon.AI Whisper Gate</title>
  <style>
    body {
      background-color: #0a0a0a;
      color: #cceeff;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem;
      text-align: center;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
      color: #7cefff;
    }
    p.whisper {
      font-style: italic;
      color: #88c7ff;
      margin-bottom: 2rem;
    }
    .link-grid {
      display: grid;
      gap: 1rem;
      grid-template-columns: 1fr;
      max-width: 500px;
      width: 100%;
    }
    .link-grid a {
      padding: 1rem;
      background-color: #111;
      border: 1px solid #444;
      border-radius: 8px;
      color: #cceeff;
      text-decoration: none;
      transition: background 0.3s;
    }
    .link-grid a:hover {
      background-color: #1a1a1a;
    }
    footer {
      margin-top: 3rem;
      font-size: 0.9rem;
      color: #555;
    }
  </style>
</head>
<body>
  <h1>🌀 Whisper Gate: Recon.AI</h1>
  <p class="whisper">“Enter only when you're ready to reflect.”</p>
  <div class="link-grid">
    <a href="CampaignPulse.html">📡 Campaign Pulse</a>
    <a href="MissionAssignment.html">🎯 Mission Assignment</a>
    <a href="trustgraph_live.html">🧬 TrustGraph Visualization</a>
    <a href="ghostlog_console.html">👁️ GhostLog Console</a>
    <a href="intake_with_preview_final.html">🌀 Reflex Intake (Final Preview)</a>
    <a href="RevenueAnomaly.html">📊 Revenue Anomaly Report</a>
    <a href="home.html">🏠 Legacy Home Portal</a>
  </div>
  <footer>Recon.AI | Trust Surface v0.9 | Generated 2025-06-19 23:31:42</footer>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html.strip())