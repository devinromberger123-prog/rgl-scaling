import matplotlib.pyplot as plt


def plot_bivariate_collapse(u_sets, y_sets, labels=None, title=None):
    """
    Plot a public RGL bivariate collapse.

    Parameters
    ----------
    u_sets : sequence of array-like
        User-supplied bivariate scaling variable values.
    y_sets : sequence of array-like
        User-supplied rescaled response values.
    labels : sequence of str, optional
        Labels for each set.
    title : str, optional
        Plot title.
    """
    if labels is None:
        labels = [None] * len(u_sets)

    for u, y, label in zip(u_sets, y_sets, labels):
        plt.scatter(u, y, label=label)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Bivariate scaling variable: u = sigma / mu^kappa")
    plt.ylabel("Rescaled response: Y = V_eff / mu^gamma")
    plt.title(title or "Response Geometry Law (RGL) Bivariate Collapse")
    if any(label is not None for label in labels):
        plt.legend()
    plt.tight_layout()
    plt.show()
