import wikipedia
import wolframalpha
import pyttsx3
client = wolframalpha.Client("4Y3AHE-HURR7XW85V")
engine = pyttsx3.init()

import PySimpleGUI as sg

engine.setProperty('rate', 140)

sg.theme('DarkPurple')

layout = [[sg.Text("Ask me anything?")],
          [sg.Input()],
          [sg.Button('Ok'), sg.Button('Quit')]]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break 
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        res = client.query(values[0])
        wolf_res = next(res.results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking("Wolfram Results: "+ wolf_res, "Wikipedia Results: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        res = client.query(values[0])
        wolf_res = next(res.results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking(wolf_res)
    except wikipedia.exceptions.PageError:
        res = client.query(values[0])
        wolf_res = next(res.results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking(wolf_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()
    print(values[0])


    # print(next(res.results).text)
    # window['-OUTPUT-'].update(next(res.results).text)
    

window.close() 