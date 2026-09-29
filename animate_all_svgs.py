import re
import glob

def inject_animation(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find width and height
    match_w = re.search(r'width="(\d+)"', content)
    match_h = re.search(r'height="(\d+)"', content)
    if not match_w or not match_h:
        print(f"Skipping {filepath} - no width/height found")
        return

    W = float(match_w.group(1))
    H = float(match_h.group(1))

    # Calculate path variables
    y_base = H * 0.85
    y_base_low = H * 0.80
    y_peak = H * 0.75
    y_dip = H * 0.95
    w25 = W * 0.25
    w50 = W * 0.50
    w100 = W

    # Generate the animated background block
    # We will inject the new defs into the existing <defs> block
    new_defs = """
    <radialGradient id="g_bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#3a2b08"/>
      <stop offset="45%" stop-color="#11100c"/>
      <stop offset="100%" stop-color="#050505"/>
    </radialGradient>
    <filter id="bg_glow">
      <feGaussianBlur stdDeviation="12" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="grid_bg" width="55" height="55" patternUnits="userSpaceOnUse">
      <path d="M55 0H0V55" fill="none" stroke="#c9a84c" stroke-opacity=".10"/>
    </pattern>
"""
    # Add new_defs inside </defs>
    content = content.replace("</defs>", new_defs + "  </defs>")

    new_bg = f"""
  <rect width="100%" height="100%" fill="url(#g_bg)"/>
  <rect width="100%" height="100%" fill="url(#grid_bg)"/>

  <g opacity=".55" filter="url(#bg_glow)">
    <circle cx="15%" cy="25%" r="2.5" fill="#fff3ad">
      <animate attributeName="cy" values="25%;15%;25%" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".2;1;.2" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="25%" cy="75%" r="2" fill="#c9a84c">
      <animate attributeName="cx" values="25%;30%;25%" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".1;.9;.1" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="75%" cy="30%" r="2.5" fill="#fff3ad">
      <animate attributeName="cy" values="30%;20%;30%" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".2;1;.2" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="85%" cy="70%" r="2" fill="#c9a84c">
      <animate attributeName="cx" values="85%;80%;85%" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values=".1;.8;.1" dur="8s" repeatCount="indefinite"/>
    </circle>
  </g>
  
  <path fill="none" stroke="#c9a84c" stroke-opacity=".35" stroke-width="1.5">
    <animate attributeName="d" dur="9s" repeatCount="indefinite"
      values="M0 {y_base} Q{w25} {y_peak} {w50} {y_base} T{w100} {y_base};
              M0 {y_base_low} Q{w25} {y_dip} {w50} {y_base_low} T{w100} {y_base_low};
              M0 {y_base} Q{w25} {y_peak} {w50} {y_base} T{w100} {y_base}"/>
  </path>
"""

    # Replace the existing solid background rect with new_bg
    # For profile_image.svg it's <rect width="960" height="960" fill="url(#bg)" rx="48" stroke="url(#gold)" stroke-width="4" />
    # For tech_matrix.svg it's <rect width="1664" height="600" fill="url(#bg)" />
    # For hero_gold.svg it's <rect width="1664" height="400" fill="url(#bgGrad)" rx="16" />
    # We will just find the first <rect width=... fill="url(#...)" ...> after </defs> and replace it.
    
    rect_pattern = r'</defs>\s*<rect[^>]*fill="url\([^>]*>'
    
    # Check if there is an rx parameter in the original rect to preserve rounded corners on the background
    match_rect = re.search(rect_pattern, content)
    if match_rect:
        original_rect = match_rect.group(0)
        
        # If it has stroke and rx, let's keep a container or add them to the outer SVG
        # The easiest way is to add a clipPath or just draw a border rect at the end.
        # But we can just inject our new_bg
        
        content = content.replace(original_rect, '</defs>\n' + new_bg)
        
        # Write back
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find background rect in {filepath}")

for f in glob.glob("assets/*.svg"):
    inject_animation(f)

