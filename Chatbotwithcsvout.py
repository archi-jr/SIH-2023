import csv
from flask import Flask, request, render_template
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pyttsx3

app = Flask("Chatbot.py")


knowledge_base_old = {
    "runny or stuffy nose, sneezing, coughing, sore throat, mild headache, fatigue": "Common Cold",
    "fever, chills, muscle aches, fatigue, cough, sore throat, congestion": "Influenza (Flu)",
    "fever, dry cough, fatigue, shortness of breath, loss of taste or smell, sore throat": "COVID-19",
    "nausea, vomiting, diarrhea, stomach cramps, fever": "Stomach Flu (Gastroenteritis)",
    "sneezing, runny or stuffy nose, itchy or watery eyes, coughing": "Allergies",
    "shortness of breath, wheezing, coughing, chest tightness": "Asthma",
    "severe headache, often one-sided, nausea, vomiting, sensitivity to light and sound": "Migraine",
    "headache, dizziness, chest pain, shortness of breath": "Hypertension (High Blood Pressure)",
    "frequent urination, excessive thirst, fatigue, blurred vision": "Diabetes",
    "cough with mucus, chest discomfort, fatigue, mild fever": "Bronchitis",
    "fever, cough with mucus, difficulty breathing, chest pain, fatigue": "Pneumonia",
    "burning sensation during urination, frequent urination, cloudy or bloody urine, abdominal pain": "Urinary Tract Infection (UTI)",
    "heartburn, regurgitation, chest pain, difficulty swallowing": "Gastroesophageal Reflux Disease (GERD)",
    # Add more questions and answers here
}


knowledge_base = {

    "runny or stuffy nose, sneezing, coughing, sore throat, mild headache, fatigue": "Common Cold",
    "fever, chills, muscle aches, fatigue, cough, sore throat, congestion": "Influenza (Flu)",
    "fever, dry cough, fatigue, shortness of breath, loss of taste or smell, sore throat": "COVID-19",
    "nausea, vomiting, diarrhea, stomach cramps, fever": "Stomach Flu (Gastroenteritis)",
    "sneezing, runny or stuffy nose, itchy or watery eyes, coughing": "Allergies",
    "shortness of breath, wheezing, coughing, chest tightness": "Asthma",
    "severe headache, often one-sided, nausea, vomiting, sensitivity to light and sound": "Migraine",
    "headache, dizziness, chest pain, shortness of breath": "Hypertension (High Blood Pressure)",
    "frequent urination, excessive thirst, fatigue, blurred vision": "Diabetes",
    "cough with mucus, chest discomfort, fatigue, mild fever": "Bronchitis",
    "fever, cough with mucus, difficulty breathing, chest pain, fatigue": "Pneumonia",
    "burning sensation during urination, frequent urination, cloudy or bloody urine, abdominal pain": "Urinary Tract Infection (UTI)",
    "heartburn, regurgitation, chest pain, difficulty swallowing": "Gastroesophageal Reflux Disease (GERD)",
    "Fatigue, Jaundice (yellowing of the skin and eyes), Dark urine, Abdominal pain, Loss of appetite, Nausea, Joint pain": "Hepatitis C",
    "Itchy skin, Redness, Rash, Dry and scaly patches, Swelling, Cracking": "Eczema (Atopic Dermatitis)",
    "Shortness of breath, Chronic cough, Wheezing, Excess mucus production": "COPD (Chronic Obstructive Pulmonary Disease)",
    "Irregular heartbeat, Rapid heartbeat, Chest pain or discomfort, Dizziness, Fatigue": "Atrial Fibrillation",
    "Abdominal bloating, Pelvic pain, Difficulty eating or feeling full quickly, Frequent urination": "Ovarian Cancer",
    "Abnormal vaginal bleeding, Pelvic pain, Pain during sex": "Cervical Cancer",
    "Frequent urination, Weak urine flow, Blood in urine or semen, Erectile dysfunction": "Prostate Cancer",
    "Fatigue, Pale skin, Frequent infections, Unexplained bruising or bleeding": "Leukemia",
    "Fatigue, Difficulty walking, Numbness or tingling, Muscle weakness, Vision problems": "Multiple Sclerosis (MS)",
    "Muscle weakness, Difficulty speaking and swallowing, Muscle cramps, Twitching": "Amyotrophic Lateral Sclerosis (ALS)",
    "Cough lasting more than 3 weeks, Chest pain, Coughing up blood, Fatigue, Weight loss, Fever, Night sweats": "Tuberculosis(TB)",
    "Fever, Chills, Sweating, Headaches, Nausea, Vomiting, Muscle pain": "Malaria",
    "Sudden high fever, Severe headaches, Joint and muscle pain, Skin rash, Bleeding": "Dengue Fever",
    "Severe diarrhea, Dehydration, Rapid heart rate, Muscle cramps, Nausea, Vomiting": "Cholera",
    "High fever, Weakness, Stomach pain, Headaches, Loss of appetite, Constipation or diarrhea": "Typhoid Fever",
    "Cough, Runny nose, Sneezing, Sore throat, Fever, Difficulty breathing": "Acute Respiratory Infections (ARI)",
    "Frequent loose stools, Dehydration, Abdominal cramps, Nausea, Vomiting": "Diarrheal Diseases",
    "Prolonged fever, Weight loss, Enlarged spleen and liver, Weakness": "Kala-Azar (Visceral Leishmaniasis)",
    "Itchy skin, Rash, Pimple-like irritations, Sores": "Scabies",
    "Muscle weakness, Rapid loss of motor skills, Difficulty swallowing": "Amyotrophic Lateral Sclerosis (ALS)",
    "Seizures, Personality changes, Memory problems, Hallucinations": "Creutzfeldt-Jakob Disease (CJD)",
    "Chronic fatigue, Joint pain, Cognitive difficulties": "Lyme Disease",
    "Severe abdominal pain, Vomiting, Blood in stool, Diarrhea": "Hemolytic Uremic Syndrome (HUS)",
    "Muscle stiffness, Tremors, Muscle spasms": "Huntington's Disease",
    "Extreme muscle weakness, Difficulty breathing": "Myasthenia Gravis",
    "Skin thickening, Joint pain, Swelling, Digestive problems": "Systemic Scleroderma",
    "Abnormal bone growth, Joint pain, Hearing loss": "Fibrodysplasia Ossificans Progressiva (FOP)",
    "Paralysis, Loss of sensation, Muscle wasting": "Guillain-Barré Syndrome (GBS)",
    "Enlarged organs, Bone pain, Fatigue, Anemia": "Gaucher Disease",
    "Memory loss, Difficulty speaking and swallowing, Muscle weakness": "Frontotemporal Dementia",
    "Severe abdominal pain, Weight loss, Malnutrition": "Chronic Intestinal Pseudo-obstruction",
    "Uncontrolled movements, Dystonia, Cognitive impairment": "Wilson Disease",
    "Extreme fatigue, Joint pain, Skin rashes": "Behçet's Disease",
    "Muscle stiffness, Joint contractures, Progressive disability": "Stiff Person Syndrome",
    "Bleeding episodes, Easy bruising, Joint pain": "Hemophilia",
    "Rapid weight loss, Fatigue, Night sweats": "Hodgkin Lymphoma",
    "Loss of coordination, Speech problems, Muscle weakness": "Friedreich's Ataxia",
    "Bone pain, Fractures, Deformities": "Osteogenesis Imperfecta (Brittle Bone Disease)",
    "Vision loss, Blind spots, Floaters, Retinal detachment": "Retinitis Pigmentosa",
    "Fever, Weight loss, Enlarged spleen and liver, Anemia, Swelling": "Black Fever (Visceral Leishmaniasis)",
    "Skin ulcers, Swelling, Pain, Fever": "Buruli Ulcer",
    "Itchy skin, Rash, Eye problems, Blindness, Skin nodules": "River Blindness (Onchocerciasis)",
    "Skin lesions, Numbness, Muscle weakness, Vision loss": "Leprosy",
    "Swelling of limbs, Fever, Chills, Skin problems": "Filariasis",
    "Painful blisters, Fever, Nausea, Vomiting": "Guinea Worm Disease (Dracunculiasis)",
    "Skin sores, Rash, Swelling, Bone pain": "Yaws",
    "Eye discharge, Itchy eyes, Eye pain, Blindness": "Trachoma",
    "Fever, Abdominal pain, Diarrhea, Blood in urine or stool, Fatigue": "Schistosomiasis",
    #"dry cough": "Influenza (Flu),COVID-19,Bronchitis,Pneumonia,COPD (Chronic Obstructive Pulmonary Disease),Tuberculosis(TB),Acute Respiratory Infections (ARI)",
}

def preprocess_input(input_text):
    input_text = input_text.lower()
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(input_text)
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    return filtered_words


def healthcare_chatbot(input_text, keywords):
    input_tokens = preprocess_input(input_text)
    max_similarity = 0
    best_match = None

    for question in knowledge_base:
        question_tokens = preprocess_input(question)
        common_tokens = set(input_tokens) & set(question_tokens)
        similarity = len(common_tokens) / len(question_tokens)

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = question

    if max_similarity >= 0.5:
        return knowledge_base[best_match]
    elif max_similarity:
        for word in keywords:
            target_value = word

            matching_keys = []

            for key, value in knowledge_base.items():
                for i in key.split():
                    i = i.lower()
                    i = i.replace(",", "")
                    if i == target_value:
                        matching_keys.append(value)

            if matching_keys:
                s = f"Illnesses containing the symptom '{target_value}' are:\n"
                for key in matching_keys:
                    s += f"{key}\n"
                return s

    else:
        return "I'm sorry, I don't have information on that topic."

@app.route('/')
def home():
    return render_template('index.html')

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() == "exit":
        return
    else:
        keywords = preprocess_input(user_input)
        response = healthcare_chatbot(user_input, keywords)

        with open("SerialNumber.txt", "r+") as f:
            a = eval(f.read())
            a += 1
            f.seek(0)
            f.write(str(a))
            with open("Symptoms and Illnesses.csv", "a+", newline = "") as f:
                csvwriter = csv.writer(f)
                csvwriter.writerow([a, user_input, response])


        SpeakText(response)
        return render_template('index.html', user_input=user_input, response=response)


app.run(debug = True)
