import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import re
import speech_recognition
import time
from call import name
#constants
v = -1
width = 0.5

#getting the province 
recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    time.sleep(0.75)
    print("\nTell us, which provinces would you like to see?")
    time.sleep(0.75)
    print("Options:\nAlberta\nBritish Columbia\nNova Scotia\nOntario\nAll\n\n")
    time.sleep(1.)
    print("I would like to see:")
    audio = recognizer.listen(source)
    choices = recognizer.recognize_google(audio)


#counting number of plots needed
if re.search("All", choices, re.IGNORECASE):
    plots = 4

elif re.search('British Columbia', choices, re.IGNORECASE):
    plots = len(re.findall(r'\w+', choices)) - 1

    if re.search('Nova Scotia', choices, re.IGNORECASE):
        plots -= 1
        
    elif re.search('And', choices, re.IGNORECASE):
        plots -= 1  

elif re.search('Nova Scotia', choices, re.IGNORECASE):
    plots = len(re.findall(r'\w+', choices))  - 1

    if re.search('British Columbia', choices, re.IGNORECASE):
        plots -= 1 
    
    elif re.search('And', choices, re.IGNORECASE):
        plots -= 1 

else:
    plots = len(re.findall(r'\w+', choices)) 

    if re.search('And', choices, re.IGNORECASE):
        plots -= 1 


#drawing the figure where the plots will be
if plots == 1 and choices.title() !='All':
    fig, ax = plt.subplots()

else:
    fig, axs = plt.subplots(plots)


# drawing each plot for a figure with multiple plot
def newAx(province):
    n = v
    x = np.arange(len(Years))

    axs[n].bar(x, Male, width, label='Male')
    axs[n].bar(x, Female, width, bottom=Male, label='Female')

    axs[n].set_ylabel('Frequency')
    axs[n].set_title(f'{name}, in {province}')    
    axs[n].set_xticks(x)
    axs[n].set_xticklabels(Years)
    axs[n].legend()

    every_nth = 4
    for n , label in enumerate(axs[n].xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
            

# drawing the plot within the figure (1 plot)
def solo(province):
    n = v
    x = np.arange(len(Years))

    ax.bar(x, Male, width, label='Male')
    ax.bar(x, Female, width, bottom=Male, label='Female')

    ax.set_ylabel('Frequency')
    ax.set_title(f'{name}, in {province}')    
    ax.set_xticks(x)
    ax.set_xticklabels(Years)
    ax.legend()

    every_nth = 4
    for n , label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    

# collect the information for each province that was chosen
if re.search("Alberta|All", choices, re.IGNORECASE):
    from Alberta import AlbertaYears, AlbertaFemale, AlbertaMale
    Years = AlbertaYears
    Female = AlbertaFemale
    Male = AlbertaMale
    v += 1
    if len(AlbertaFemale) == 0:
        print(f"{name} does not appear in the Alberta, Female name database.")

    if len(AlbertaMale) == 0:
        print(f"{name} does not appear in the Alberta, Male name database.")

    if len(choices.split()) == 1 and choices.title() != 'All':
        solo('Alberta')
    
    else:
        newAx('Alberta')
 

if re.search("B(ritish)? C(olumbia)?|BC|All", choices, re.IGNORECASE):
    from BC import BCYears, BCFemale, BCMale
    Years = BCYears
    Female = BCFemale
    Male = BCMale
    v += 1
    if len(BCFemale) == 0:
        print(f"{name} does not appear in the British Columbia, Female name database.")

    if len(BCMale) == 0:
        print(f"{name} does not appear in the British Columbia, Male name database.")

    if plots == 1 and choices.title() != 'All':
        solo('British Columbia')
    
    else:
        newAx('British Columbia')

if re.search("N(ova)? S(cotia)?|NS|All", choices, re.IGNORECASE):
    from NS import NSYears, NSFemale, NSMale
    Years = NSYears
    Female = NSFemale
    Male = NSMale
    v += 1
    if len(NSFemale) == 0:
        print(f"{name} does not appear in the Nova Scotia, Female name database.")

    if len(NSMale) == 0:
        print(f"{name} does not appear in the Ontario, Male name database.")

    if len(choices.split()) == 1 and choices.title() != 'All':
        solo('Nova Scotia')
    
    else:
        newAx('Nova Scotia')
    
if re.search("Ontario|All", choices, re.IGNORECASE):
    from Ontario import OntarioYears, OntarioFemale, OntarioMale
    Years = OntarioYears
    Female = OntarioFemale
    Male = OntarioMale
    v += 1
    if len(OntarioFemale) == 0:
        print(f"{name} does not appear in the Ontario, Female name database.")

    if len(OntarioMale) == 0:
        print(f"{name} does not appear in the Ontario, Male name database.")
    if len(choices.split()) == 1 and choices.title() != 'All':
        solo('Ontario')
    
    else:
        newAx('Ontario')


# printing the figure
fig.tight_layout()
plt.get_current_fig_manager().window.state('zoomed')
plt.show()