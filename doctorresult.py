

medicine_dict = {
    "common cold": ["Rest", "Hydration", "Over-the-counter cold medications"],
    "influenza (Flu)": ["Rest", "Hydration", "Antiviral medications (prescribed by a doctor)"],
    "COVID-19": ["Isolation", "Hydration", "Symptom management (consult a healthcare provider)"],
    "stomach flu (Gastroenteritis)": ["Oral rehydration solution", "Antiemetic medications (for nausea and vomiting)"],
    "allergies": ["Antihistamines", "Decongestants", "Corticosteroids (for severe allergies)"],
    "asthma": ["Bronchodilators", "Inhaled corticosteroids (for long-term control)"],
    "migraine": ["Pain relievers (e.g., ibuprofen)", "Triptans (for severe migraines)"],
    "hypertension (High Blood Pressure)": ["Antihypertensive medications (prescribed by a doctor)"],
    "diabetes": ["Insulin or oral antidiabetic medications (as prescribed by a doctor)"],
    "bronchitis": ["Rest", "Hydration", "Cough suppressants"],
    "pneumonia": ["Antibiotics (as prescribed by a doctor)", "Rest", "Hydration"],
    "urinary tract infection (UTI)": ["Antibiotics (as prescribed by a doctor)", "Hydration"],
    "gastroesophageal reflux disease (GERD)": ["Antacids", "Proton pump inhibitors (PPIs)"],
    "hepatitis C": ["Antiviral medications (prescribed by a doctor)"],
    "eczema (Atopic Dermatitis)": ["Topical corticosteroids", "Moisturizers"],
    "COPD (Chronic Obstructive Pulmonary Disease)": ["Bronchodilators", "Inhaled corticosteroids"],
    "atrial fibrillation": ["Antiarrhythmic medications (prescribed by a doctor)"],
    "ovarian cancer": ["Surgery", "Chemotherapy", "Radiation therapy (as prescribed by an oncologist)"],
    "cervical cancer": ["Surgery", "Chemotherapy", "Radiation therapy (as prescribed by an oncologist)"],
    "prostate cancer": ["Surgery", "Radiation therapy", "Hormone therapy (as prescribed by an oncologist)"],
    "leukemia": ["Chemotherapy", "Radiation therapy (in some cases)", "Bone marrow transplant (in some cases)"],
    "multiple sclerosis (MS)": ["Disease-modifying therapies (as prescribed by a neurologist)"],
    "amyotrophic lateral sclerosis (ALS)": ["Riluzole", "Supportive care for symptoms"],
    "tuberculosis(TB)": ["Antibiotics (as prescribed by a doctor)", "Directly Observed Therapy (DOT)"],
    "malaria": ["Antimalarial medications (as prescribed by a doctor)"],
    "dengue fever": ["Supportive care for symptoms", "Pain relievers (e.g., acetaminophen)"],
    "cholera": ["Oral rehydration solution", "Antibiotics (in severe cases)"],
    "typhoid fever": ["Antibiotics (as prescribed by a doctor)", "Hydration"],
    "acute respiratory Infections (ARI)": ["Rest", "Hydration", "Symptom management"],
    "diarrheal diseases": ["Oral rehydration solution", "Antidiarrheal medications (in some cases)"],
    "japanese encephalitis": ["Supportive care for symptoms", "Vaccination (for prevention)"],
    "kalaazar (Visceral Leishmaniasis)": ["Antiprotozoal medications (as prescribed by a doctor)"],
    "scabies": ["Scabicide creams or lotions (as prescribed by a doctor)"],
    "creutzfeldt-Jakob Disease (CJD)": ["Supportive care for symptoms"],
    "lyme Disease": ["Antibiotics (as prescribed by a doctor)"],
    "hemolytic Uremic Syndrome (HUS)": ["Supportive care for symptoms", "Dialysis (in severe cases)"],
    "huntington's Disease": ["Symptomatic treatment", "Supportive care"],
    "myasthenia Gravis": ["Cholinesterase inhibitors", "Immunosuppressants"],
    "systemic Scleroderma": ["Immunosuppressants", "Symptomatic treatment"],
    "fibrodysplasia Ossificans Progressiva (FOP)": ["Symptomatic treatment", "Physical therapy"],
    "guillain-Barré Syndrome (GBS)": ["Intravenous immunoglobulin (IVIG)", "Plasma exchange (plasmapheresis)"],
    "gaucher Disease": ["Enzyme replacement therapy (as prescribed by a doctor)"],
    "frontotemporal Dementia": ["Symptomatic treatment", "Supportive care"],
    "chronic Intestinal Pseudo-obstruction": ["Symptomatic treatment", "Nutritional support"],
    "wilson Disease": ["Chelating agents", "Liver transplantation (in severe cases)"],
    "behçet's Disease": ["Immunosuppressants", "Anti-inflammatory medications"],
    "stiff Person Syndrome": ["Muscle relaxants", "Physical therapy"],
    "hemophilia": ["Clotting factor replacement therapy (as prescribed by a doctor)"],
    "hodgkin Lymphoma": ["Chemotherapy", "Radiation therapy (as prescribed by an oncologist)"],
    "friedreich's Ataxia": ["Symptomatic treatment", "Physical therapy"],
    "osteogenesis Imperfecta (Brittle Bone Disease)": ["Fracture management", "Physical therapy"],
    "retinitis Pigmentosa": ["Symptomatic treatment", "Low vision aids"],
    "black Fever (Visceral Leishmaniasis)": ["Antiprotozoal medications (as prescribed by a doctor)"],
    "buruli Ulcer": ["Antibiotics (as prescribed by a doctor)", "Wound care"],
    "river Blindness (Onchocerciasis)": ["Antiparasitic medications (as prescribed by a doctor)"],
    "leprosy": ["Multidrug therapy (as prescribed by a doctor)"],
    "filariasis": ["Antiparasitic medications (as prescribed by a doctor)"],
    "guinea Worm Disease (Dracunculiasis)": ["Pain management", "Wound care"],
    "yaws": ["Antibiotics (as prescribed by a doctor)"],
    "trachoma": ["Antibiotics (as prescribed by a doctor)"],
    "schistosomiasis": ["Antiparasitic medications (as prescribed by a doctor)"],
}
dis=input("the disease: ")
if dis in medicine_dict:
    medicine=medicine_dict[dis]
    prescribed=input("the specific medicine: ")
    final_med=[s.replace("as prescribed by a doctor",prescribed) for s in medicine]
    morning=input("morning")
    afternoon=input("afternoon")
    evening=input("evening")
    night=input("night")
    final_medi=" ".join(final_med)
    print(final_medi + " dosage: "+"M:"+morning+" AF:"+afternoon + " E:" + evening + " N:" + night)

