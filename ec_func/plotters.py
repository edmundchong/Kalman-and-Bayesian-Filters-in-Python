def plot_measurements(ax, xs, ys=None, dt=None, color='k', lw=1, label='Measurements',
                      lines=False, **kwargs):
    """ Helper function to give a consistent way to display
    measurements in the book.
    """
    if ys is None and dt is not None:
        ys = xs
        xs = np.arange(0, len(ys)*dt, dt)


    if lines:
        if ys is not None:
            return ax.plot(xs, ys, color=color, lw=lw, ls='--', label=label, **kwargs)
        else:
            return ax.plot(xs, color=color, lw=lw, ls='--', label=label, **kwargs)
    else:
        if ys is not None:
            return ax.scatter(xs, ys, edgecolor=color, facecolor='none',
                        lw=2, label=label, **kwargs),
        else:
            return ax.scatter(range(len(xs)), xs, edgecolor=color, facecolor='none',
                        lw=2, label=label, **kwargs),



def plot_filter(ax, df, z_col, x_col, pred_col=None, actual_col=None):


    if not isinstance(x_col, list):
        x_col = [x_col]

    for this_x_col in x_col:
        ax.plot(df.index, df[this_x_col], marker='o', label=this_x_col)

    if pred_col is not None:
        ax.plot(df.index, df[pred_col], c='r', marker='v', linestyle='--', label='Predictions')
    if actual_col is not None:
        ax.plot(df.index, df[actual_col], c='k', lw=1, label='Actual')

    plot_measurements(ax, df.index, df[z_col], color='k', lines=False,label='Measurements')

    ax.set_xlabel('Time step')
    ax.set_ylabel('State')
    ax.legend(loc=4)
