import numpy as NP
import matplotlib.colors as COLORMAP
import matplotlib.pyplot as PLT

class Color:
    """
    Color : Collection of colors for visulization
    """
    ## Color defination ##
    ### standard
    white=[1,1,1,1]
    black=[0,0,0,1]
    dark=[0.16793541, 0.16793541, 0.16793541, 1.]
    blue=[6/255, 154/255, 243/255, 1.] #xkcd:azure
    midnight = [0.09, 0.18, 0.23, 1.]
    richblue = [0.14, 0.43, 0.96, 1.]
    heroblue = [0.37, 0.84, 0.98, 1.]
    darkblue = [31/255, 99/255, 99/255, 1.]
    teal = [0.42, 0.87, 0.66, 1.]
    herogreen = [0.78, 0.86, 0.29, 1.]
    hotgreen = [0.91, 0.99, 0.37, 1.]
    #warm= [0.87, 0.45, 0.43, 1.]
    warm = [0.98, 0.46, 0.19, 1.]
    hot = [1., 0.05, 0.23, 1.]
    powergreen=[40/255, 238/255, 44/255, 1.]
    ## monet
    monetblue=[87/255, 160/255, 253/255, 1.]
    monetteal=[136/255, 234/255, 253/255, 1.]
    monetgreen=[136/255, 234/255, 99/255, 1.]
    monetyellow=[255/255, 239/255, 82/255, 1.]
    monetorange=[255/255, 191/255, 48/255, 1.]
    monetpink=[255/255, 153/255, 167/255, 1.]
    monetred=[255/255, 121/255, 181/255, 1.]
    monetpurple=[181/255, 72/255, 255/255, 1.]

    ## Color list ##
    colors = {'white':white,
              'black':black,
              'dark':dark,
              'blue':blue,
              'midnight':midnight,
              'richblue':richblue,
              'heroblue':heroblue,
              'teal':teal,
              'herogreen':herogreen,
              'hotgreen':hotgreen,
              'powergreen':powergreen,
              'warm':warm,
              'hot':hot
              'monetpurple':monetpurple,
              'monetred':monetred,
              'monetpink':monetpink,
              'monetorange':monetorange,
              'monetyellow':monetyellow,
              'monetgreen':monetgreen,
              'monetteal':monetteal,
              'monetblue':monetblue}

    ## colors method ##
    @classmethod
    def adjustColor(cls, color, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect color with add / subtract ratio

        Parameters
            color : array-like (N,4), N number of color codes (r, g, b, a) to be adjusted
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            adjusted_color : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """
        color = NP.atleast_2d(color).astype(float)
        ## adjust each color ##
        color[:,0] = color[:,0]*(1+delta_r)
        color[:,1] = color[:,1]*(1+delta_g)
        color[:,2] = color[:,2]*(1+delta_b)
        color[:,3] = color[:,3]*(1+delta_a)
        ## fix with the limit ##
        color[color > 1] = 1
        color[color < 0] = 0
        ## output ##
        nrow = color.shape[0]
        if nrow == 1:
            return color.tolist()[0]
        else:
            return color.tolist()

    @classmethod
    def getWhite(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('white', cls.white)
        return cls.adjustColor(cls.white, delta_r, delta_g, delta_b, delta_a)


    @classmethod
    def getBlack(delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('black', cls.black)
        return cls.adjustColor(cls.black, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getDark(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('dark', cls.dark)
        return cls.adjustColor(cls.dark, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getBlue(delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('blue', cls.blue)
        return cls.adjustColor(cls.blue, delta_r, delta_g, delta_b, delta_a)


    @classmethod
    def getMidnight(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('midnight', cls.midnight)
        return cls.adjustColor(cls.midnight, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getRichblue(delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """
        Adjuect %s:%s with add / subtract ratio
        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('richblue', cls.richblue)
        return cls.adjustColor(cls.richblue, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getHeroblue(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('heroblue', cls.heroblue)
        return cls.adjustColor(cls.heroblue, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getTeal(delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('teal', cls.teal)
        return cls.adjustColor(cls.teal, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getHerogreen(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('herogreen', cls.herogreen)
        return cls.adjustColor(cls.herogreen, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getHotgreen(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('hotgreen', cls.hotgreen)
        return cls.adjustColor(cls.hotgreen, delta_r, delta_g, delta_b, delta_a)

    def getWarm(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('warm', cls.warm)
        return cls.adjustColor(cls.warm, delta_r, delta_g, delta_b, delta_a)

    @classmethod
    def getHot(cls,delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('hot', cls.hot)
        return cls.adjustColor(cls.hot, delta_r, delta_g, delta_b, delta_a)

    def getPowerGreen(cls, delta_r=0, delta_g=0, delta_b=0, delta_a=0):
        """Adjuect %s:%s with add / subtract ratio

        Parameters
            delta_r : float, adjustion ratio of red. The output limit of alpha is 0 <= red <= 1 (default 0)
            delta_g : float, adjustion ratio of green. The output limit of alpha is 0 <= green <= 1 (default 0)
            delta_b : float, adjustion ratio of blue. The output limit of alpha is 0 <= blue <= 1 (default 0)
            delta_a : float, adjustion ratio of alpha. The output limit of alpha is 0 <= alpha <= 1 (default 0)
        OUTPUT
            color_code : : array-like (N,4), N number of adjusted color codes (r*(1+delta_r), g*(1+delta_g), b*(1+delta_b), a*(1+delta_a)) 
        """%('powergreen', cls.powergreen)
        return cls.adjustColor(cls.powergreen, delta_r, delta_g, delta_b, delta_a)


    ## Member functions ##
    @classmethod
    def getClist(cls, color_names, colors=colors):
        """Get color list with input name

        Parameters
            color_names : string array-like, name of colors
            colors : array-like, list of color codes of color_names
        OUTPUT
            ckeys : list, name list of color list
            clist : list, color code of name list
        """
        ckeys = []
        clist = []
        for key in color_names:
            if key in colors.keys():
                ckeys.append(key)
                clist.append(colors[key])
            else:
                print('>> [WANRING] color name "%s" not found and skip'%key)
        return ckeys, clist

    @classmethod
    def getCmap(cls, color_lists, n=100, name='', empty_begin=True):
        """Get matplotlib colormap

        Parameters
            color_lists : list, color lists for the referance of color map
            n           : int, number of segments of color
            name        : string, name of cmap
            empty_begin : boolen, make begin color is transparents
        OUTPUT
            cmap : maplotlib.color
        """
        name = str(name)
        if name == '':
            name = '_colormap'
        ## make cmap
        cmap = COLORMAP.LinearSegmentedColormap.from_list(name, list(color_lists), N=n)
        #if empty_begin:
        #    cmap = 
        return cmap

    @classmethod
    def keys(cls):
        """
        list the existed color names
        """
        return list(cls.colors.keys())

    @classmethod
    def values(cls):
        """
        list the existed color codes
        """
        return list(cls.colors.values())

    ## Gogoro Colors ##
    ckeys_standard = ['midnight','richblue','heroblue','teal','herogreen','hotgreen','warm','hot']
    ckeys_standard, clist_standard = getClist(ckeys_standard)
    cmap_standard = getCmap(clist_standard, name='standard', n=100)

    ckeys_standard_light = ['richblue','heroblue','teal','herogreen','hotgreen','warm','hot']
    ckeys_standard_light, clist_standard_light = getClist(ckeys_standard_light)
    cmap_standard_light = getCmap(clist_standard_light, name='standard_light', n=100)

    ckeys_monet_light = ['monetblue','monetteal','monetgreen','monetyellow','monetorange','monetpink', 'monetred']
    ckeys_monet_light, clist_standard_light = getClist(ckeys_monet_light)
    cmap_monet_light = getCmap(clist_monet_light, name='standard_light', n=100)


