import re
import glob

# I'll just git checkout the files to start clean!
import os
os.system("git checkout assets/*.svg")

def inject_animation(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find width and height
    match_w = re.search(r'width="(\d+)"', content)
    match_h = re.search(r'height="(\d+)"', content)
    W = float(match_w.group(1))
    H = float(match_h.group(1))

    y_base = H * 0.85
    y_base_low = H * 0.80
    y_peak = H * 0.75
    y_dip = H * 0.95
    w25 = W * 0.25
    w50 = W * 0.50
    w100 = W

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
    content = content.replace("</defs>", new_defs + "  </defs>")

    # Find the main rect
    rect_pattern = r'</defs>\s*(<rect[^>]*fill="url\([^>]*>)'
    match_rect = re.search(rect_pattern, content)
    if not match_rect:
        return
        
    original_rect = match_rect.group(1)
    
    # We want to replace the fill of the original rect with our g_bg to preserve rx, stroke, etc.
    # And then we duplicate it for the grid
    rect_g_bg = re.sub(r'fill="[^"]+"', 'fill="url(#g_bg)"', original_rect)
    rect_grid = re.sub(r'fill="[^"]+"', 'fill="url(#grid_bg)"', original_rect)
    
    # Wait, the grid doesn't need stroke because the base one has it.
    rect_grid = re.sub(r'stroke="[^"]+"', '', rect_grid)
    rect_grid = re.sub(r'stroke-width="[^"]+"', '', rect_grid)

    new_bg = f"""
  {rect_g_bg}
  {rect_grid}

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
    content = content.replace("</defs>\n  " + original_rect, "</defs>\n" + new_bg)
    content = content.replace("</defs>\n" + original_rect, "</defs>\n" + new_bg)

    with open(filepath, 'w') as f:
        f.write(content)

for f in glob.glob("assets/*.svg"):
    inject_animation(f)

