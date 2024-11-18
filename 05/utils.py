import matplotlib
from matplotlib import pyplot as plt

def preparefigure(f):
    plt.figure(figsize=(8,4))
    plt.xlim(-3*f,3*f)
    plt.ylim(-1.5*f,1.5*f)
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
