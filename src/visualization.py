import matplotlib.pyplot as plt


def plot_graph(df, x_col, y_col, compare_col=None):

    if compare_col:
        pivot_df = df.pivot(
            index=x_col,
            columns=compare_col,
            values=y_col
        )
        pivot_df.plot()
        plt.title("Data Analysis")

    else:
        plt.scatter(df[x_col], df[y_col])
        plt.title("Data Analysis")

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()