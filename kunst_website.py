import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_embedcode import github_gist

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
               height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def read(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        return lines

with st.sidebar:
    selection_screen = option_menu("Kunst", ["Home", "Überblick", "Gutes", "Schlechtes", "Beispiel", "Tagebuch", "Reflexion"],
                                   icons=["house", "app-indicator", "plus-circle", "dash-circle", "journal-code", "journal", "body-text"],
                                   menu_icon="bank")
    st.image("./images/logo_kunst.png")
if selection_screen == "Home":
    st.title("Home")
    st.video("./images/Einleitung.mp4")
    st.text("Gemacht von Lorenz Rutkevich")

elif selection_screen == "Überblick":
    st.title("Neuronale Netzwerke im Überblick")
    st.video("./images/NeuralNet.mp4")
    st.markdown("#### Neuronale Netze sind eine Klasse von künstlichen Intelligenz-Modellen, die auf dem Konzept von Neuronen im menschlichen Gehirn basieren. Diese Modelle können komplexe Muster in großen Datenmengen lernen und Vorhersagen treffen. Ein neuronales Netz besteht aus drei Hauptteilen: dem Input-Layer, dem Hidden-Layer und dem Output-Layer. Das Input-Layer nimmt die Eingangsdaten (z.B. ein Bild mit x und y Koordinaten) auf und bereitet sie für das Netzwerk vor. Das Hidden-Layer verarbeitet die Daten und identifiziert wichtige Muster und Trends. Es besteht aus einer Vielzahl von Neuronen, die miteinander verbunden sind und Informationen aus dem Input-Layer verarbeiten. Das Output-Layer gibt die Vorhersage oder Klassifizierung des neuronalen Netzes aus. Es kann aus einem oder mehreren Neuronen bestehen, die aufgrund ihrer Verbindungen zum Hidden-Layer eine Vorhersage treffen. Zusammen arbeiten diese Schichten im neuronalen Netz zusammen, um eine Vorhersage auf Grundlage der Eingangsdaten zu treffen. Es ist wichtig zu beachten, dass die genaue Architektur und Anzahl der Neuronen in jeder Schicht für eine bestimmte Aufgabe optimiert werden kann. In diesem Artikel habe ich einen Überblick über die grundlegenden Teile eines neuronalen Netzes gegeben. Es gibt jedoch noch viele weitere wichtige Konzepte und Technologien im Zusammenhang mit neuronalen Netzen, aber dies sollte einen guten Einstieg in das Thema bieten und meine Frage beantworten.")

elif selection_screen == "Gutes":
    st.title("KI bringt viel gutes")
    st.markdown("#### Neuronale Netze können eine Vielzahl von Aufgaben ausführen, darunter:")
    st.markdown("#### 1. Klassifikation: Dies beinhaltet das Zuordnen von Eingabedaten zu vordefinierten Kategorien oder Klassen, wie beispielsweise bei der Erkennung von Gesichtern oder dem Klassifizieren von Nachrichten in bestimmte Themen.")
    st.markdown("#### 2. Regression: Hier geht es darum, eine kontinuierliche Ausgabe anhand von Eingabedaten zu schätzen, z.B. Vorhersagen des Hauspreises auf der Grundlage von Merkmalen wie Größe, Lage und Alter.")
    st.markdown("#### 3. Computer Vision: Hier werden neuronale Netze eingesetzt, um Bilder und Videos zu verarbeiten und wichtige Merkmale wie Gesichter, Objekte und Bewegungen zu erkennen.")
    st.markdown("#### 4. Naturliche Sprachverarbeitung (NLP): Hier können neuronale Netze verwendet werden, um Texte und Sprache zu analysieren, wie z.B. Sentimentanalyse, Übersetzungen oder Textgenerierung.")
    st.markdown("#### 5. Spielerische Anwendungen: Hierbei können neuronale Netze eingesetzt werden, um Computerspiele zu spielen und gegen menschliche Spieler anzutreten, wie beispielsweise bei Spielen wie Schach oder Go.")
    st.markdown("#### Neuronale Netze sind ein wichtiger Teil der Künstlichen Intelligenz und können eine Vielzahl von Aufgaben ausführen. Sie können auch Menschen auf vielen Gebieten unterstützen, wie Gesundheit, Bildung, Finanzen, Verkehr und Unterhaltung. Durch die Fähigkeit, große Datenmengen zu analysieren und Entscheidungen zu treffen, die sonst für den Menschen schwer oder unmöglich zu treffen wären, können Neuronale Netze einen wertvollen Beitrag zur Verbesserung unserer Welt leisten.")


elif selection_screen == "Schlechtes":
    st.title("Aber nicht alles ist gut")
    st.markdown("#### Es gibt einige Nachteile und Herausforderungen bei der Verwendung von neuronalen Netzen, darunter:")
    st.markdown("#### 1. Überanpassung: Wenn ein neuronales Netzwerk zu sehr auf einen bestimmten Datensatz trainiert wird, kann es schlecht auf neue, unbekannte Daten generalisieren.")
    st.markdown("#### 2. Interpretierbarkeit: Es kann schwierig sein, die Entscheidungen eines neuronalen Netzes zu verstehen und zu interpretieren, da sie auf komplexen Verbindungen und Gewichtungen zwischen Neuronen basieren.")
    st.markdown("#### 3. Datenanforderungen: Um ein neuronales Netzwerk effektiv trainieren zu können, ist es erforderlich, große Mengen an qualitativ hochwertigen Daten bereitzustellen.")
    st.markdown("#### 4. Bias: Neuronale Netze können einen Bias aufweisen, wenn sie auf biased-Datensätzen trainiert werden, was zu ungenauen oder unfairen Entscheidungen führen kann.")
    st.markdown("#### Künstliche Intelligenz und Neuronale Netze bergen einige Risiken, darunter:")
    st.markdown("- #### Datenschutz: Die Verwendung von neuronalen Netzen erfordert oft den Zugriff auf große Mengen an sensiblen Daten, was zu Datenschutzproblemen führen kann. ")
    st.markdown("- #### Jobverlust: Die Automatisierung durch KI und neuronale Netze kann dazu führen, dass bestimmte Arbeitsplätze überflüssig werden.")
    st.markdown("- #### Fehler und unerwartete Ausgänge: Neuronale Netze können aufgrund ihrer Komplexität und mangelnden Interpretierbarkeit Fehler verursachen oder unerwartete Ergebnisse liefern, insbesondere in kritischen Anwendungsbereichen wie beispielsweise im medizinischen Bereich oder bei autonomen Systemen wie Drohnen.")
    st.markdown("- #### Unethische Entscheidungen: KI-Systeme können aufgrund ihrer Programmierung oder aufgrund von Bias in den Datensätzen unethische Entscheidungen treffen.")
    st.markdown("#### Es ist wichtig, dass bei der Entwicklung und Anwendung von KI und neuronalen Netzen die möglichen Risiken sorgfältig abgewogen und entsprechende Maßnahmen ergriffen werden, um diese zu minimieren. Dazu gehören beispielsweise Regulierungen, Überwachung und Transparenz, Ethikrichtlinien und Verantwortung. Es ist eine kontinuierliche Herausforderung, KI und neuronale Netze so zu entwickeln und einzusetzen, dass sie den größtmöglichen Nutzen bringen und gleichzeitig sicher und verantwortungsvoll sind.")
    st.markdown("#### Instanzen wie zum Beipsiel die EU haben diesbezüglich jedoch schon Maßnahmen ergriffen, welche man zum Beispiel [hier](https://algorithmwatch.org/de/europarat-kunstliche-intelligenz/) nachlesen kann.")
elif selection_screen == "Beispiel":
    st.title("Beispiel eines Klassifizierungsnetzes")
    github_gist("https://gist.github.com/lorenz-7/a5c85ce29a40fb9a5b168102a7b9e8e8")
    st.markdown("#### Dieses Modell ist ein tiefes neuronales Netz, das für die Klassifikation von Bildern verwendet wird – zur Zeit der Vorstellung lieferte es bahnbrechende Neuerungen. Es besteht aus mehreren Schichten:")
    st.markdown("#### 1. Conv2D-Schichten: Diese Schichten führen Konvolutionen aus, bei denen das Eingabebild mit Filtern überlappt wird, um Merkmale zu erkennen.")
    st.markdown("#### 2. MaxPooling2D-Schichten: Diese Schichten führen Max-Pooling aus, bei dem ein Teilbereich des Bildes ausgewählt wird, um die Dimensionen des Eingabebilds zu reduzieren und gleichzeitig wichtige Merkmale zu erhalten.")
    st.markdown("#### 3. Flatten-Schicht: Diese Schicht flattet die Ausgabe der Konvolution und Pooling-Schichten.")
    st.markdown("#### 4. Dense-Schichten: Diese Schichten sind vollständig verbundene Schichten, die das Modell trainieren.")
    st.markdown("#### 5. Output-Schicht: Die Output-Schicht gibt Wahrscheinlichkeiten bezogen auf den Input wieder.")
    st.markdown("#### Zusammen bilden diese Schichten ein Modell, das in der Lage ist, aus Eingabebildern Merkmale zu extrahieren und diese Merkmale zur Klassifikation zu verwenden.")


elif selection_screen == "Tagebuch":
    st.title("Mein Wekstatt-Tagebuch")
    for i in reversed(range(16)):
       if i != 0:
           st.image(f"./images/{i}.jpg")
            
elif selection_screen == "Reflexion":
    st.title("Reflexion")
    st.markdown('##### Meine Werkstattarbeit hatte das Thema "Wie kann "Kunst" in Interaktion mit der Natur helfen?". Durch diese Arbeit konnte ich viele Erfahrungen sammeln und Probleme aufdecken. Aufgrund meiner Vorerfahrungen und Interessen entschied ich mich, eine Website zu erstellen, die meine Ausarbeitung darstellt. Zunächst wollte ich ein Video erstellen, aber aufgrund der Komplexität und des geringen Nutzens habe ich mich für den Kompromiss entschieden, Videos in meine Website zu integrieren. Nach zwei Wochen beschloss ich, eine Blog-Website zu gestalten, und nutzte dazu das Framework¹ Streamlit, das mit der Programmiersprache Python funktioniert.')
    st.markdown("##### Während des Entwicklungsprozesses meiner Website musste ich mich immer wieder mit schwierigen Problemen auseinandersetzen. Insbesondere die Integration von Textteilen in den Code erwies sich als knifflig. Ich musste auch ständig darauf achten, dass das Design und Layout der Website benutzerfreundlich und attraktiv sind. Durch die Lösung dieser Herausforderungen konnte ich meine Fähigkeiten im Bereich Webdesign und -entwicklung verbessern.")
    st.markdown("##### Trotz der Herausforderungen verlief die Arbeit insgesamt sehr gut. Ich konnte das Logo und das Layout der Website erfolgreich entwerfen und durch meine Erfahrungen in diesem Bereich konnte ich auftretende Probleme schneller lösen. Auch konnte ich meine Fähigkeiten im Bereich der Zusammenarbeit verbessern, indem ich regelmäßig Feedback von anderen einholte.")
    st.markdown("##### Insgesamt bin ich sehr zufrieden mit dieser Arbeit und konnte auch große Fortschritte beim selbstständigen Lernen, Zeitmanagement und spontaner Problemlösung verzeichnen. Die Arbeit hat mir gezeigt, wie wichtig es ist, ein starkes Fundament an Wissen und Fähigkeiten zu haben, um Herausforderungen zu meistern. Obwohl ich viel durch diese Arbeit gelernt habe, wurden auch viele meiner Probleme aufgedeckt. Ich bin froh, dass ich diese Erfahrungen machen konnte und ich bin zuversichtlich, dass ich meine neu erworbenen Fähigkeiten in Zukunft anwenden werde.")
    st.markdown("---")
    st.markdown("¹ Ein Grundgerüst, welches die Arbeit vereinfacht.")
    


    
