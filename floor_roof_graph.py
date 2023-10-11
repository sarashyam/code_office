import os # used to get the files in a folder 
import glob # used to access all the .csv files 
import matplotlib.pyplot as plt # to plot the graph
import pandas as pd # to manipulate the data
import random # to randomly choose a value

color_floor = 0 # index for choosing color for floor
color_roof = 0 # index for choosing color for roof
#-------------******successfull************_---------------------
#--------------------------- read roof---------------------------
def read_roof(file_name):
    df_roof = pd.read_csv(file_name,skiprows=[0,2])
    df_roof.tail(-1)
    df_roof['X'] = df_roof['X'].astype(float)
    df_roof['STNy'] = df_roof['STNy'].astype(float)
    x_roof = df_roof['X']
    y_roof = df_roof['STNy']
    print(x_roof,y_roof)
    global color_roof
    draw_graph(x_roof,y_roof,0,file_name,color_roof)
    color_roof = color_roof + 1
#---------------------------read floor-------------

def read_floor(file_name):
    df_floor = pd.read_csv(file_name,skiprows=[0,2]) # to read the rows and skip the 0 and 2nd row in csv file
    df_floor.tail(-1) # removing the last row of the csv file
    df_floor['X'] = df_floor['X'].astype(float) # converting to float values so as to do the calcuations
    df_floor['STNy'] = df_floor['STNy'].astype(float)
    x_floor = df_floor['X'] #setting the varialbe with the x values  as x axis
    y_floor = df_floor['STNy'] #setting the varialbe with the STNy values  as y axis
    print(x_floor,y_floor) # just printing in console to verify the values
    global color_floor # to access the global variable
    draw_graph(x_floor,y_floor,1,file_name, color_floor) # calling draw_graph function to create the graph
    color_floor = color_floor + 1 # to give the index of color to be choosen from list


#--------------------------draw graph--------------------------

def draw_graph(x,y,i,file_name,color_graph):
    colorblue=['royalblue','dodgerblue','deepskyblue','skyblue','#6483C8'] # color for roof 
    colorgreen=['darkolivegreen', 'green','limegreen','yellowgreen','lightseagreen'] # color for floor
    legend_name = os.path.basename(file_name) # displays the name of the file in the graph according to the lines plotted
    m=[",","o","v","^","<",">"] # to randomly choose the values for marker

    if i == 0:
        floor = colorblue[color_graph]# color_graph is the index that will choose the color from the colorblue list
        ax[i].plot(x,y,label=legend_name,marker=random.choice(m),linewidth=0.5,color=floor,markersize=2.8)
        ax[i].set_title('ROOF') # title of the graph

    if i == 1:
        roof = colorgreen[color_graph] # color_graph is the index that will choose the color from the colorgreen list
        ax[i].plot(x,y,label=legend_name,marker=random.choice(m),linewidth=0.5,color=roof,markersize=2.8) # to plot the graph
        ax[i].set_title('FLOOR') # title of the graph

    ax[i].set_ylabel('STNy kN/m^2')
    ax[i].set_facecolor('lightgrey')  # Set the background color
    ax[i].set_ylim(-2500, 100)
    ax[i].grid(linestyle=":",color="green",axis ='y') # only create y axis 
    ax[i].axhline(0, color='red',linestyle="-",linewidth=0.6) # to make a red line at index 0
    #legend_name = os.path.basename(file_name)
    ax[i].legend(loc="lower center",fontsize=8) # to display 

# ----------------------to find file and give into specific lists--------------


fig,ax = plt.subplots(2,1,figsize=(11.69,8.27))

c_path = os.getcwd()
files = os.listdir(c_path) # storing all the files in 'files' 
#print(files)
#print("-------------------------------------------------------------")
csv_files = glob.glob(c_path + "/*.csv") # finding all the files with .csv extension

#csv_files = glob.glob(c_path + "/*.csv")
#print(csv_files)

roof_file =[] # will store roof named files
floor_file =[] # will store floor named files
r = "Roof" # string which will be matched with the file name
f = "Floor"



for fl in csv_files:
    # print(fl)
    if r in fl:
        #roof_file.append(fl)
        read_roof(fl) # to get the roof files


        
    elif f in fl:
        read_floor(fl) # to get the floor files
        #floor_file.append(fl)
        


# print(roof_file)
# print("-------------------------------------------------------------")
# print(floor_file)
#plt.grid(axis='y')
plt.savefig('plot_trial_roof_floor.pdf', format='pdf') # to save figure in pdf format
plt.show() # to show the graph in the window






