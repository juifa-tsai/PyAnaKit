import numpy as NP
import matplotlib.pyplot as PLT
import matplotlib.transforms as Transforms
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.patches import Ellipse

## local modules
from .color import Color 


class Historgram:
    """
    historgram functional namespace
    """

    @classmethod
    def hist1(cls, data, xbins, xmin, xmax, ylim=None, weights=None, overflow=True, normal=False, title='', legend=False, error=True, cdf=False, color='std'):
        """Draw 1-D histogram with PDF and CDF

        Parameters
        ----------
        data : array-like 
            data to be draw
        xbins : int
            Number of bins of x-axis
        xmin : float
            Minimum range of x-axis
        xmax : float 
            Maximum range of x-axis
        ylim : list
            Y-axis limits (default None)
        weights : array-like
            weight of data (default None)
        title : str 
            Title of histogram (default '')
        legend      : boolen / string, location of legend, e.g. 'best' (default False)
        overflow    : boolen, if include the data out of range (default True)
        normal      : boolen, if normalize histogram (default False)
        error       : boolen, get error (default True)
        cdf         : boolen, get cdf (default False)

        Returns
        -------
        fig
            matplotlib.figure 
        """
        ## 
        data = NP.atleast_1d(data)
        ## 
        if isinstance(color, str) and color.find('monet') >= 0:
            color_hist = Color.monetteal
            color_cdf = Color.monetpink
        else:
            color_hist = Color.blue
            color_cdf = Color.powergreen

        ## weights
        if weights is None:
            sumw2 = False
            weights = NP.ones(data.shape)
            mean = NP.mean(data)
            std  = NP.std(data)
        else:
            sumw2 = True
            weights = NP.atleast_1d(weights)
            mean = NP.sum(data*weights)/NP.sum(weights)
            std  = NP.sqrt(NP.sum(((data - mean)**2)*weights)/NP.sum(weights)) 
        ## overflow option
        if overflow:
            data = NP.clip(data, xmin, xmax)
        ## create figure
        fig, ax1 = PLT.subplots(figsize=PLT.gcf().get_size_inches())

        ## PDF ##
        ## style setting
        ax1.set_title(title, fontsize=15, y=1.03)
        ax1.tick_params(labelsize=15)
        ax1.set_xlim([xmin,xmax])
            
        ## Normalization option
        integral = 1.
        if normal:
            msk = (data <= xmax) & (data >= xmin)
            integral = weights[msk].sum()
            
        ## draw histogram
        y, x = NP.histogram(data, bins=xbins, range=[xmin,xmax], weights=weights)
        y = NP.insert(y, 0, 0)
        ax1.plot(x, y/integral, ls='steps', color=color_hist)
        ax1.fill_between(x, y/integral, step="pre", alpha=0.4, color=color_hist, label=r'PDF $\mu = %.3f\pm%.3f$'%(mean, std))
        
        # Draw error bar
        yerr = NP.zeros(y.shape)
        if error:
            if sumw2:
                sumw2 = NP.histogram(data, bins=xbins, range=[xmin,xmax], weights=weights**2)
                yerr = NP.sqrt(NP.insert(sumw2[0], 0, 0))/integral
            else:
                yerr = NP.sqrt(y)/integral
            xerr = NP.array(x) - NP.abs(x[1]-x[0])/2.
            ax1.errorbar(xerr, y/integral, yerr=yerr, color=color_hist, fmt='none')
        
        ## get handel
        if ylim is not None:
            ax1.set_ylim(ylim)
        else:
            ax1.set_ylim([0, (y/integral+yerr).max()*1.1])
        handel1, label1 = ax1.get_legend_handles_labels()

        ## CDF ##
        ## caculate cdf
        if cdf:
            y = NP.array([y[:i+1].sum()/weights.sum() for i in range(len(y))]) 
            x = NP.linspace(xmin, xmax, xbins+1)
            x_halfcdf = x[NP.argmin(NP.abs(y - 0.5))]
            ## set label
            label = r'CDF'
            if x_halfcdf > xmin:
                label += r', x = %.3f (CDF$_{1/2}$)'%x_halfcdf
            else:
                label += r', CDF$_{min}$ = %.3f'%NP.min(y)
            ## set style
            ax2 = ax1.twinx()
            ax2.tick_params(labelsize=15)
            ax2.set_ylim([0, 1.1])
            ## draw plot
            ax2.plot(x, y, '-', ls='steps', color=color_cdf, label=label, linewidth=2)
            handel2, label2 = ax2.get_legend_handles_labels()

        ## add legend
        if legend:
            if cdf:
                PLT.legend([handel1[0], handel2[0]], [label1[0], label2[0]] , frameon=False, fontsize=13, title_fontsize=13, loc = legend if isinstance(legend, str) else 'best')
            else:
                PLT.legend(frameon=False, fontsize=13, title_fontsize=13, loc=legend if isinstance(legend, str) else 'best')
        return


    @classmethod
    def hist2(cls, x, y, xbins, xmin, xmax, ybins, ymin, ymax, # must
                    # options
                    vmin=None,
                    vmax=None, 
                    weights=None, 
                    normal=False,
                    correlation=False, 
                    overflow=True,
                    zero_to_nan=True,
                    colorbar = True,
                    xtitle='', 
                    ytitle='',
                    cmap=None,
                    grid=None,
                    diagonal=False,
                    ellipse=False,
                    showmean=False,
                    showmax=False,
                    **styles ):
        """
        2D histogram and calculate correlation
        INPUT
            x           : array-like (n,), n data for x-axis value
            y           : array-like (n,), n data for y-axis value
            xbins       : int, number of bins of x-axis
            xmin        : float, minimum ragne of x-axis
            xmax        : float, maximum range of x-axis
            ybins       : int, number of bins of y-axis
            ymin        : float, minimum ragne of y-axis
            ymax        : float, maximum range of y-axis
            vmin        : float, maximum of z-value (defualt None)
            vmax        : float, minimum of z-value (defualt None)
            weights     : array-like (xbins, ybins), weight of bins (defualt None)
            normal      : boolen, normalization (default False)
            correlation : boolen, if True, the correlation is calcualted and show on title. (defualt False)
            overflow    : boolen, if True, overflow data to the last bin for x & y-axis (defualt True)
            zero_to_nan : boolen, if True, zero value will be empty (defualt True)
            colorbar    : boolen, show colorbar (defualt True)
            xtitle      : string, title of x-axis (defualt '')
            ytitle      : string, title of y-axis (defualt '')
            cmap        : matplotlib.colors, color map for 2d plots
            ellipse     : boolen, draw peason ellipse confidence
            showmean    : boolen, draw mean point
            showmax     : boolen, draw maximum point 
            **style     : arguments of matplotlib.pyplot.imshow
        OUTPUT
            correlation : float, if correlation == True
            None, if correlation == False
        """
        x = NP.atleast_1d(x)
        y = NP.atleast_1d(y)

        ## open figure
        figsize = PLT.gcf().get_size_inches()
        fig, ax = PLT.subplots(figsize=figsize)

        # overflow bin
        if overflow:
            x = NP.clip(x, xmin, xmax)
            y = NP.clip(y, ymin, ymax)

        # get histogram
        h, xe, ye = NP.histogram2d(x, y, bins=(xbins, ybins), range=[[xmin, xmax], [ymin, ymax]], weights=weights)

        # set correlation
        if correlation:
            if weights is None:
                corr = NP.corrcoef(x,y)[1,0]
            else:
                # weighted counts
                hs = h.sum(axis=0)
                # expected values of x-axis
                ys = (h*ye[:-1][:,NP.newaxis]).sum(axis=0)
                ys = NP.divide(ys, hs, out=NP.zeros_like(ys), where=(hs!=0))
                # x-axis
                xs = xe[:-1]
                # no zero case
                msk = ys != 0
                corr = NP.corrcoef(xs[msk],ys[msk])[1,0]
            ax.set_title('Correlation : %.2f'%corr, fontsize=15)
            
        # rotate h
        h = NP.flip(h, axis=1).T
        ye = NP.flip(ye) 
            
        # draw mod
        if showmax:
            hmod = NP.unravel_index(NP.argmax(h), h.shape)
            ax.plot(xe[hmod[1]]+NP.abs(xe[1]-xe[0])/2, 
                    ye[hmod[0]]-NP.abs(ye[1]-ye[0])/2, 
                    "o",
                    markerfacecolor='none',
                    markersize=NP.mean(figsize), 
                    markeredgewidth=NP.mean(figsize)/6,
                    color=Color.midnight)
            
        if showmean:
            ax.plot(x.mean(), 
                    y.mean(),
                    "o",
                    markersize=NP.mean(figsize), 
                    color=Color.midnight)
        
        if ellipse:
            cov = NP.cov(x, y)
            pearson = cov[0, 1]/NP.sqrt(cov[0, 0] * cov[1, 1])
            # Using a special case to obtain the eigenvalues of this
            width  = NP.sqrt(1 + pearson) * 2
            height = NP.sqrt(1 - pearson) * 2
            mean_x = NP.mean(x)
            mean_y = NP.mean(y)
            n_stds = [1] if isinstance(ellipse, bool) else NP.array(ellipse)
            for n_std in n_stds:
                if n_std <= 0: 
                    continue
                scale_x = NP.sqrt(cov[0, 0]) * n_std
                scale_y = NP.sqrt(cov[1, 1]) * n_std
                transf = Transforms.Affine2D().rotate_deg(45).scale(scale_x, scale_y).translate(mean_x, mean_y)
                ellipse_ax = Ellipse((0, 0), width=width, height=height, facecolor='none', edgecolor=Color.midnight, linewidth=NP.mean(figsize)/5, linestyle=':')
                ellipse_ax.set_transform(transf + ax.transData)
                ax.add_patch(ellipse_ax)
        
        # draw 2D
        ## set paramater
        if normal:
            h = h / h.sum()
        if vmin is None:
            vmin = h.min()
        if vmax is None:
            vmax = h.max()
        if isinstance(cmap, str) and cmap.find('monet') >= 0:
            cmap = Color.cmap_monet_light
        else:
            cmap = Color.cmap_standard_light
        if zero_to_nan:
            h[h == 0] = None
        img = ax.imshow(h, extent=[xmin, xmax, ymin, ymax], cmap=cmap, vmax=vmax, vmin=vmin, aspect='auto', **styles)

        # styling
        ax.tick_params(labelsize=15)
        ax.set_xlabel(xtitle, fontsize=15)
        ax.set_ylabel(ytitle, fontsize=15)
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        
        # set grid
        if grid is not None:
            if isinstance(grid, str):
                if grid.lower() == 'x':
                    ax.grid(axis='x')
                elif grid.lower() == 'y':
                    ax.grid(axis='x')
                else:
                    ax.grid(axis='both')
            else:
                ax.grid(axis='both')

        if diagonal:
            if diagonal < 0:
                ax.plot([xmin, xmax], [ymax, ymin], '-', color='gray', linewidth=0.6)
            else:
                ax.plot([xmin, xmax], [ymin, ymax], '-', color='gray', linewidth=0.6)
        
        # make colorbar
        if colorbar:
            from mpl_toolkits.axes_grid1 import make_axes_locatable
            cax = make_axes_locatable(ax).append_axes("right", size="5%", pad=0.1)
            PLT.colorbar(img, cax=cax)
            
        # return correlation
        if correlation:
            return corr
        else:
            return

