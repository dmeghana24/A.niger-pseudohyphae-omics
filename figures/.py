
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(13, 4))
ax.axis('off')

steps = [
    "Literature\nMining",
    "Sample\nCollection",
    "RNA/Protein\nExtraction",
    "RNA-seq\nAnalysis",
    "Proteomics\nAnalysis",
    "Gene-Protein\nMapping",
    "Integration &\nEnrichment",
    "Validation",
    "Output"
]

x = list(range(len(steps)))
for i, step in enumerate(steps):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x[i], 0), 1, 0.6, boxstyle="round,pad=0.08",
        fc="#cce5ff", ec="#3399ff", lw=2
    ))
    ax.text(x[i]+0.5, 0.3, step, va='center', ha='center', fontsize=11)
    if i < len(steps)-1:
        ax.arrow(x[i]+0.95, 0.3, 0.1, 0, head_width=0.08, head_length=0.08, fc='k', ec='k')

ax.set_xlim(-0.5, len(steps))
ax.set_ylim(-0.2, 1)
plt.tight_layout()
plt.savefig("../figures/pipeline_overview.png", dpi=200)
plt.show()
