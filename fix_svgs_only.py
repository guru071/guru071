import re

with open("README.md", "r") as f:
    c = f.read()

# Replace What I focus on list
focus_old = """### What I focus on

- 🚀 Product development
- 🌐 Web applications
- 🤖 AI & automation
- 🔧 Software engineering
- 🎨 Modern UI/UX
- 🧪 Technology experiments
- 📱 Digital products"""
focus_new = """### What I focus on
<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=20&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=600&lines=🚀+Product+development;🌐+Web+applications;🤖+AI+&+automation;🔧+Software+engineering;🎨+Modern+UI/UX;🧪+Technology+experiments;📱+Digital+products" />
</div>"""
c = c.replace(focus_old, focus_new)

# Replace PROJECT ECOSYSTEM tables (just the inner contents of cells)
c = re.sub(
    r'## 🛒 MaghGo\s+GOAT\'ECH project focused on building a modern digital product experience\.\s*<a href="https://maghgo\.goatech\.tech">\s*<img src="https://img\.shields\.io/badge/OPEN_MAGHGO-111111\?style=for-the-badge" />\s*</a>',
    r"""<a href="https://maghgo.goatech.tech">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=22&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=400&lines=🛒+MaghGo;Modern+Digital+Product;Click+To+Open+→" />
</a>""", c, flags=re.DOTALL)

c = re.sub(
    r'## 🗳️ TN Voting\s+A digital voting project exploring secure, transparent voting workflows\.\s*<a href="https://tnvoting\.goatech\.tech">\s*<img src="https://img\.shields\.io/badge/OPEN_TN_VOTING-c9a84c\?style=for-the-badge&labelColor=111111" />\s*</a>',
    r"""<a href="https://tnvoting.goatech.tech">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=22&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=400&lines=🗳️+TN+Voting;Secure+Voting+Workflows;Click+To+Open+→" />
</a>""", c, flags=re.DOTALL)

c = re.sub(
    r'## 🌊 Aqua\s+A project within the GOAT\'ECH technology ecosystem\.\s*<a href="https://aqua\.goatech\.tech">\s*<img src="https://img\.shields\.io/badge/OPEN_AQUA-c9a84c\?style=for-the-badge&labelColor=111111" />\s*</a>',
    r"""<a href="https://aqua.goatech.tech">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=22&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=400&lines=🌊+Aqua;Technology+Ecosystem;Click+To+Open+→" />
</a>""", c, flags=re.DOTALL)

c = re.sub(
    r'## 💻 Nothing IDE\s+A concept around a modern development environment\.\s*<a href="https://github\.com/guru071">\s*<img src="https://img\.shields\.io/badge/VIEW_ON_GITHUB-111111\?style=for-the-badge" />\s*</a>',
    r"""<a href="https://github.com/guru071">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=22&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=400&lines=💻+Nothing+IDE;Modern+Development;Click+To+View+→" />
</a>""", c, flags=re.DOTALL)

# Replace More projects table
more_proj_old = """| Project | Focus |
|---|---|
| 🚦 **Traffic** | Real-time verification |
| 🌱 **Agritech** | Agricultural technology |
| 🧾 **Billing** | Billing software |
| 🔥 **Flames ERC** | Technology experimentation |"""
more_proj_new = """<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=22&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=800&lines=🚦+Traffic+-+Real-time+verification;🌱+Agritech+-+Agricultural+technology;🧾+Billing+-+Billing+software;🔥+Flames+ERC+-+Technology+experimentation" />
</div>"""
c = c.replace(more_proj_old, more_proj_new)

# Replace BUILD PHILOSOPHY tree
philosophy_old = """```text
                         GURUPRASATH
                              │
                              ▼
                          GOAT'ECH
                              │
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
             IDEA           BUILD         EXPERIMENT
               │              │              │
               └──────────────┼──────────────┘
                              ▼
                           IMPROVE
                              │
                              ▼
                           CREATE
```"""
philosophy_new = """<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:c9a84c,50:fff3ad,100:c9a84c&height=30&text=GURUPRASATH&fontSize=16&fontColor=111111" /><br>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&color=c9a84c&center=true&vCenter=true&width=200&lines=⬇" /><br>
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:c9a84c,50:fff3ad,100:c9a84c&height=40&text=GOAT'ECH&fontSize=20&fontColor=111111" /><br>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&color=c9a84c&center=true&vCenter=true&width=200&lines=⬇" /><br>
<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=22&duration=3000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=800&lines=IDEA++++|++++BUILD++++|++++EXPERIMENT" /><br>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&color=c9a84c&center=true&vCenter=true&width=200&lines=⬇" /><br>
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:c9a84c,50:fff3ad,100:c9a84c&height=40&text=IMPROVE&fontSize=18&fontColor=111111" /><br>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&color=c9a84c&center=true&vCenter=true&width=200&lines=⬇" /><br>
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:c9a84c,50:fff3ad,100:c9a84c&height=40&text=CREATE&fontSize=22&fontColor=111111" />
</div>"""
c = c.replace(philosophy_old, philosophy_new)

# Engineering With Purpose paragraph -> SVG
engineering_old = """<h2>Engineering With Purpose</h2>

<p>
I design and build modern software systems across the
<strong>frontend, backend, cloud, data, and AI layers.</strong>
</p>

<p>
My focus is on turning complicated product requirements into
clean, scalable, secure, and maintainable systems that are ready
for real-world production environments under <b>GOAT'ECH (MAGH'S Technology)</b>—my core group and unified company.
</p>

<br>

<table>
<tr>
<td>

<strong>Frontend</strong><br> <sub>React · Next.js · TypeScript</sub>

</td>
<td>

<strong>Backend</strong><br> <sub>Python · Node.js · Express · NestJS</sub>

</td>
</tr>

<tr>
<td>

<strong>Cloud</strong><br> <sub>AWS · Azure · Docker · Linux</sub>

</td>
<td>

<strong>AI</strong><br> <sub>Gemini · RAG · Automation</sub>

</td>
</tr>
</table>"""
engineering_new = """<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=25&duration=3500&pause=1000&color=c9a84c&center=true&vCenter=true&repeat=true&width=600&lines=Engineering+With+Purpose;Designing+modern+software+systems;Frontend,+Backend,+Cloud,+Data,+AI;Clean,+scalable,+secure+architecture" />
<br>
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=16&duration=2000&pause=500&color=ffdf73&center=true&vCenter=true&repeat=true&width=600&lines=Frontend:+React,+Next.js,+TypeScript;Backend:+Python,+Node.js,+Express;Cloud:+AWS,+Docker,+Linux;AI:+Gemini,+RAG,+Automation" />
</div>"""
c = c.replace(engineering_old, engineering_new)

with open("README.md", "w") as f:
    f.write(c)

