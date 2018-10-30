import numpy
from matplotlib import pyplot

g = 9.81
zt = 100.0

def twoDimEulerMethod(t0,T,dt,u0):
    """t0 : valeur initiale de t
       T : valeur finale de t
       dt : intervalle de temps
       u0 : condition initial sur u à t = t0
       Résout une équation du type u'(t) = f(u,t) où u est dans R^n
       """

    N = int((T-t0) / dt) + 1  # number of time steps
    t = numpy.linspace(t0, T, num=N)  # time grid
    u = numpy.array(u0)
    z = numpy.zeros(N)
    z[0] = u0[1]

    for n in range(1, N):
        u = u + dt * numpy.array([u[1], g * (1 - u[0] / zt)])
        z[n] = u[0]

    return [t,z]

    def EulerMethodPlot(t,z):
    # Set the font family and size to use for Matplotlib figures.
    pyplot.rcParams['font.family'] = 'serif'
    pyplot.rcParams['font.size'] = 16

    # Plot the solution of the elevation.
    pyplot.figure(figsize=(9.0, 4.0))  # set the size of the figure
    pyplot.title('Elevation of the phugoid over the time')  # set the title
    pyplot.xlabel('Time [s]')  # set the x-axis label
    pyplot.ylabel('Elevation [m]')  # set the y-axis label
    pyplot.xlim(t[0], t[-1])  # set the x-axis limits
    pyplot.ylim(40.0, 160.0)  # set the y-axis limits
    pyplot.grid()  # set a background grid to improve readability
    pyplot.plot(t, z, color='C0', linestyle='-', linewidth=2);

z0 = 100.0  # altitude
b0 = 10.0  # upward velocity resulting from gust

a = twoDimEulerMethod(0.0,100.0,0.02,[z0,b0])
EulerMethodPlot(a[0],a[1])
