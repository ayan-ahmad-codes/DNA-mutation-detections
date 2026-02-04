import matplotlib.pyplot as plt

def plot_mutations(mutations, dna_length):
    fig, ax = plt.subplots(figsize=(9, 2))

    ax.set_xlim(0, dna_length)
    ax.set_ylim(0, 1)

    if mutations:
        ax.scatter(
            mutations,
            [0.5] * len(mutations),
            c="red",
            s=30,
            label="Mutation"
        )

    ax.set_title(f"Mutation Map (Total: {len(mutations)})")
    ax.set_xlabel("DNA Base Pair Position")
    ax.set_yticks([])

    plt.tight_layout()
    return fig
