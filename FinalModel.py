'''
Amy Green - 200930437
5990M: Introduction to Programming for Geopgraphical Information Analysis - Core Skills
Assignment 1: Building a Simple Agent Based Model (ABM)
_version 1.0_

This model implements the agent framework within a Graphical User Interface (GUI) which utilises a run menu bar. 
A window will appear when the code is run titled 'Model'; to run the model select the run option in the top left corner.
Data has been scraped from a web page to initiate the starting locations of the agents. 
The agents will move randomly throughout the environment, eating and storing it and sharing with their neighbours until the stopping condition is reached. 
'''

import random
import matplotlib.pyplot
import agentframework
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation
import tkinter
import requests
import bs4
#matplotlib.use('tkinter')

##############################################################################
'''STEP 1 - Obtain Web Data'''

#Web Scraping - initialised with data from the web that allocates starting locations of the agents. 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) #Check that y agents were running
#print(td_xs) #Check that x values were running


##############################################################################
'''STEP 2 - Determine Parameters'''

num_of_agents = 10 #Amount of agents within the environment
num_of_iterations = 100 #Loop the agents' coordinations 100 times 
neighbourhood = 20 #Generate a neighbourhood to constructe behavioural communication. 
agents = [] #Setting up an operator list for the agents


##############################################################################
'''STEP 3 - Initialise the GUI Window'''

#Main GUI Window
root = tkinter.Tk() 
#Generating Model within GUI window  
root.wm_title("Model")
#Set up the figure and axes
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
            
            
##############################################################################
'''STEP 4 - Generate environment via a 2D List (contains spatial data that the agents will move around in)'''

f=open("in.txt")
environment = []
for line in f: 
    parsed_line = str.split(line, ",") #Seperate values by commas 
    rowlist = []
    for word in parsed_line: 
        rowlist.append(float(word))
    environment.append(rowlist) # Append all lists individually so can print environment
f.close()
#print(environment) #- Test environment and that all lines run 

##Show the environment
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99) 
matplotlib.pyplot.imshow(environment)

carry_on = True


##############################################################################
'''STEP 5 - Initialise the Agents'''

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text) #Use y locations from scraped web page
    x = int(td_xs[i].text) #Use x locations from scraped web page
    agents.append(agentframework.Agent(environment, agents, i, y, x))
    
    
############################################################################## 
'''STEP 6 - Animate the agents'''

#Uses the matplot lib animation function and updates the animated display
def update(frame_number):
    
    fig.clear() #Clears anything within the figure
    global carry_on
    
    
#Show the environment within the new display with a fixed axes 
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299) 
    
    matplotlib.pyplot.imshow(environment)
    

# Move the agents and make them interact.Pulls out agents using an index. 
    #random.shuffle(agents) - Shuffles the agents
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        
#Plot the agents within the environment for the animation      
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        #print (agents[i]._x, agents[i]._y)


#Apply a stopping condition if agents exceed the self.store 
    if random.random() < 0.001:
        carry_on = False
        print("stopping condition")


#Provides a stopping control for the animation 
def gen_function(b = [0]):
    a = 0 
    global carry_on
    while (a<100) & (carry_on) :  #Continues to work as long as carry_on is True
        yield a #Returns control and waits nect call. 
        a = a +1 


##############################################################################
'''STEP 6 - Run the GUI animated plot'''

#This generates the 'Run' GUI menu option in the figure 
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


#Sets up GUI window with TkInter - creates window and menu option
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
#model_menu.entryconfig("Run Model", state="normal")
model_menu.add_command(label="Run Model", command=run)

tkinter.mainloop()
##############################################################################

'''n.b: A second window named 'Figure' will also appear but this can be ignored.'''

'''END OF MODEL'''


