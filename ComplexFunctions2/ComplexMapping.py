from numpy import *
import matplotlib.pyplot as plt
from os import listdir, getcwd, remove

def MakePlot(Domain, xmin, xmax, ymin, ymax):

    #Sin = [sin(p[0] + p[1]*1j) for p in Domain]
    #F22 = [(1-cos(p[0] + p[1]*1j))/(1+cos(p[0] + p[1]*1j)) for p in Domain]
    Mobius = [(1j-(z[0] + z[1]*1j))/((z[0] + z[1]*1j)+1j) for z in Domain]
    #Mobius = [1j*(z-1j)/(z+1j) for z in Sin]
    cm = plt.cm.get_cmap('RdYlBu')
    fig = plt.figure()
    fig.suptitle('Mobius(w)')
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.title.set_text('Domain')
    ax1.set_xlim([xmin, xmax])
    ax1.set_ylim([ymin, ymax])
    ax2.set_xlim([-3, 3])
    ax2.set_ylim([-3, 3])
    ax2.title.set_text('Range')
    for ii,x in enumerate(Domain):
        #ax1.scatter(Sin[ii].real,Sin[ii].imag,c = cm(pi/2 - abs(x[0])))#c=cm(ii/len(Domain)))
        ax1.scatter(x[0],x[1], c=cm(ii/len(Domain)))
        ax2.scatter(Mobius[ii].real,Mobius[ii].imag, c=cm(ii/len(Domain)))
        #ax2.scatter(F22[ii].real,F22[ii].imag,c = cm(pi/2 - abs(x[0])))#c=cm(ii/len(Domain)))
        #ax2.scatter(Sin[ii].real,Sin[ii].imag,c = cm(pi/2 - abs(x[0])))#c=cm(ii/len(Domain)))

    plt.savefig("sin.png")
    return


def main():
    if __name__ == "__main__":

        points = 250

        Horizontal = linspace(-10, 10, points)
        Vertical = linspace(-10, 10, points)
        ComplexDomain = [[x,y] for x in Horizontal for y in Vertical]
        #ComplexDomain = linspace(-1.0,1.0,points)
        MakePlot(ComplexDomain, -10, 10, -10, 10)
        return

main()

